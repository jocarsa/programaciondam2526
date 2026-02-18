#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import json
import time
import sys
import os
import re
import shutil
from datetime import timedelta
from typing import Any, Dict, List, Optional, Tuple

# ============================================================
# CONFIG
# ============================================================

MODEL = "qwen2.5:3b-instruct"
INPUT_TXT = "convertido.txt"
OUTPUT_JSONL = "entrenamiento.jsonl"

# Goal: squeeze as much info as possible from the txt:
# - generate multiple Q/A per chunk
# - use overlap to avoid boundary loss
# - robust parsing + repair + retries
QA_PER_CHUNK = 6                 # how many Q/A items per chunk (typical 4-10)
CHUNK_SIZE = 1400                # characters per chunk (soft target)
CHUNK_OVERLAP = 240              # overlap between consecutive chunks
MIN_CHUNK = 500                  # avoid too small chunks when possible
MAX_CHUNK = 2200                 # cap chunk size if paragraphs are huge

# Resilience
MAX_RETRIES = 4
RETRY_BACKOFF_BASE = 1.6         # exponential backoff base
OLLAMA_TIMEOUT = 240             # seconds per call (safety)
REPAIR_ATTEMPT = True            # second call to "repair" invalid output
MAX_OUTPUT_ITEMS_PER_CALL = 20   # guardrail if model returns too many items

# Quality / coverage
DEDUP = True
NORMALIZE_WHITESPACE = True

# Files
BAD_OUTPUTS_FILE = "entrenamiento.bad.txt"   # diagnostics for invalid outputs
STATE_FILE = "entrenamiento.state.json"      # resume support

# Console
SHOW_LAST_QA_PREVIEW = True
PROGRESS_BAR_WIDTH = 28

# ============================================================
# UTIL
# ============================================================

def term_width(default: int = 100) -> int:
    try:
        return shutil.get_terminal_size((default, 20)).columns
    except Exception:
        return default

def fmt_td(seconds: float) -> str:
    if seconds < 0:
        seconds = 0
    return str(timedelta(seconds=int(seconds)))

def bar(progress: float, width: int) -> str:
    progress = max(0.0, min(1.0, progress))
    filled = int(round(progress * width))
    return "█" * filled + "░" * (width - filled)

def safe_preview(s: str, max_len: int = 140) -> str:
    s = " ".join((s or "").split())
    if len(s) <= max_len:
        return s
    return s[: max_len - 1] + "…"

def normalize_text(s: str) -> str:
    if not NORMALIZE_WHITESPACE:
        return s
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    # collapse excessive whitespace inside lines, keep paragraph breaks
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def jdump(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False)

def stable_key(q: str, a: str) -> str:
    # simple dedup key
    qn = " ".join((q or "").lower().split())
    an = " ".join((a or "").lower().split())
    return qn[:240] + "||" + an[:480]

# ============================================================
# CHUNKING (paragraph-aware + overlap)
# ============================================================

def split_paragraphs(text: str) -> List[str]:
    text = normalize_text(text)
    if not text:
        return []
    parts = re.split(r"\n\s*\n", text)
    parts = [p.strip() for p in parts if p.strip()]
    return parts

def make_chunks(paragraphs: List[str]) -> List[str]:
    """
    Build chunks by packing paragraphs into ~CHUNK_SIZE, with guardrails.
    Then apply overlap by characters to reduce boundary loss.
    """
    chunks: List[str] = []
    buf: List[str] = []
    buf_len = 0

    def flush():
        nonlocal buf, buf_len
        if not buf:
            return
        chunk = "\n\n".join(buf).strip()
        if chunk:
            chunks.append(chunk)
        buf, buf_len = [], 0

    for p in paragraphs:
        p = p.strip()
        if not p:
            continue

        # If paragraph is gigantic, slice it into smaller parts.
        if len(p) > MAX_CHUNK:
            flush()
            start = 0
            while start < len(p):
                end = min(len(p), start + MAX_CHUNK)
                sub = p[start:end].strip()
                if sub:
                    chunks.append(sub)
                start = end
            continue

        if buf_len + len(p) + (2 if buf else 0) <= CHUNK_SIZE or buf_len < MIN_CHUNK:
            buf.append(p)
            buf_len += len(p) + (2 if buf_len else 0)
        else:
            flush()
            buf.append(p)
            buf_len = len(p)

    flush()

    # Apply overlap (character-based) by prepending tail of previous chunk
    if CHUNK_OVERLAP > 0 and len(chunks) > 1:
        overlapped: List[str] = []
        prev_tail = ""
        for i, ch in enumerate(chunks):
            if i == 0:
                overlapped.append(ch)
            else:
                prev = overlapped[-1]
                tail = prev[-CHUNK_OVERLAP:]
                merged = (tail + "\n\n" + ch).strip()
                overlapped.append(merged)
        chunks = overlapped

    return chunks

# ============================================================
# OLLAMA CALLS
# ============================================================

def call_ollama(prompt: str) -> Tuple[str, str, int, float]:
    """
    Returns: (stdout, stderr, returncode, elapsed_seconds)
    """
    t0 = time.time()
    try:
        p = subprocess.run(
            ["ollama", "run", MODEL],
            input=prompt,
            text=True,
            capture_output=True,
            timeout=OLLAMA_TIMEOUT,
        )
        dt = time.time() - t0
        return (p.stdout.strip(), (p.stderr or "").strip(), p.returncode, dt)
    except subprocess.TimeoutExpired as e:
        dt = time.time() - t0
        out = (e.stdout or "").strip() if hasattr(e, "stdout") else ""
        err = (e.stderr or "").strip() if hasattr(e, "stderr") else ""
        return (out, (err + "\nTIMEOUT").strip(), 124, dt)
    except Exception as e:
        dt = time.time() - t0
        return ("", f"EXCEPTION: {e}", 125, dt)

# ============================================================
# ROBUST JSON EXTRACTION / VALIDATION
# ============================================================

def strip_code_fences(s: str) -> str:
    s = s.strip()
    # remove ```json ... ``` or ``` ... ```
    s = re.sub(r"^\s*```(?:json)?\s*", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\s*```\s*$", "", s)
    return s.strip()

def find_balanced_json_candidates(s: str) -> List[str]:
    """
    Extract JSON object/array candidates from messy text by balanced braces/brackets.
    Returns candidates in appearance order (best effort).
    """
    s = strip_code_fences(s)

    candidates: List[str] = []

    def scan(open_ch: str, close_ch: str) -> None:
        stack = 0
        start = None
        in_str = False
        esc = False
        for i, ch in enumerate(s):
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            else:
                if ch == '"':
                    in_str = True
                    continue
                if ch == open_ch:
                    if stack == 0:
                        start = i
                    stack += 1
                elif ch == close_ch and stack > 0:
                    stack -= 1
                    if stack == 0 and start is not None:
                        candidates.append(s[start:i+1])

    # Prefer arrays first if present (often model returns list)
    scan("[", "]")
    scan("{", "}")

    # Keep unique in order
    seen = set()
    out: List[str] = []
    for c in candidates:
        c2 = c.strip()
        if c2 and c2 not in seen:
            seen.add(c2)
            out.append(c2)
    return out

def parse_qa_items(raw: str) -> Tuple[Optional[List[Dict[str, str]]], Optional[str]]:
    """
    Accept:
    - {"question": "...", "answer": "..."}
    - [{"question": "...", "answer": "..."}, ...]
    Also tolerates extra keys; we keep only question/answer.
    """
    raw = strip_code_fences(raw)

    # First attempt: direct json
    try:
        obj = json.loads(raw)
        items = normalize_items(obj)
        if items is not None:
            return items, None
    except Exception:
        pass

    # Second attempt: try candidates from messy output
    candidates = find_balanced_json_candidates(raw)
    for cand in candidates:
        try:
            obj = json.loads(cand)
            items = normalize_items(obj)
            if items is not None:
                return items, None
        except Exception:
            continue

    return None, "Could not parse valid JSON with required fields"

def normalize_items(obj: Any) -> Optional[List[Dict[str, str]]]:
    # dict -> list
    if isinstance(obj, dict):
        obj = [obj]
    if not isinstance(obj, list):
        return None

    items: List[Dict[str, str]] = []
    for it in obj:
        if not isinstance(it, dict):
            continue
        q = it.get("question")
        a = it.get("answer")
        if isinstance(q, str) and isinstance(a, str):
            q = q.strip()
            a = a.strip()
            if q and a:
                items.append({"question": q, "answer": a})

    if not items:
        return None

    # Guardrail
    if len(items) > MAX_OUTPUT_ITEMS_PER_CALL:
        items = items[:MAX_OUTPUT_ITEMS_PER_CALL]

    return items

# ============================================================
# PROMPTS
# ============================================================

def build_prompt(chunk: str, n_items: int) -> str:
    """
    Strong instructions:
    - strict JSON only
    - return ARRAY of objects
    - extract as many distinct facts as possible
    - avoid generic questions
    - questions must be answerable from chunk
    """
    return f"""
Eres un generador de dataset de entrenamiento para un LLM.
Tu tarea: extraer INFORMACIÓN del texto y convertirla en preguntas/respuestas (Q/A) útiles y específicas.

REGLAS IMPORTANTES:
- Responde SIEMPRE en español.
- SOLO puedes usar información que esté explícitamente en el texto.
- NO inventes datos. NO añadas contexto externo.
- Evita preguntas genéricas tipo “¿Qué es...?” si el texto no lo define.
- Prioriza hechos, definiciones, pasos, requisitos, excepciones, listas, ejemplos, conceptos clave.
- Cada pregunta debe ser respondible solo con este texto.

FORMATO DE SALIDA (JSON ESTRICTO, sin texto adicional):
Devuelve un ARRAY JSON con EXACTAMENTE {n_items} elementos.
Cada elemento: {{"question":"...","answer":"..."}}
No incluyas claves extra. No incluyas markdown. No incluyas comentarios.

TEXTO:
\"\"\"
{chunk}
\"\"\"
""".strip()

def build_repair_prompt(bad_output: str) -> str:
    return f"""
Convierte el contenido siguiente en JSON ESTRICTO únicamente.
Devuelve SOLO:
- Un objeto {{"question":"...","answer":"..."}} o
- Un array de objetos con esas claves.
Sin markdown, sin texto adicional, sin claves extra.

Contenido a convertir:
\"\"\"
{bad_output}
\"\"\"
""".strip()

# ============================================================
# RESUME / STATE
# ============================================================

def load_state() -> Dict[str, Any]:
    if not os.path.exists(STATE_FILE):
        return {}
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f) or {}
    except Exception:
        return {}

def save_state(state: Dict[str, Any]) -> None:
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(jdump(state))
    os.replace(tmp, STATE_FILE)

def count_jsonl_lines(path: str) -> int:
    if not os.path.exists(path):
        return 0
    n = 0
    with open(path, "r", encoding="utf-8") as f:
        for _ in f:
            n += 1
    return n

# ============================================================
# CONSOLE
# ============================================================

def print_header(total_chars: int, total_chunks: int, resume_from: int) -> None:
    w = term_width()
    line = "─" * min(w, 120)
    print(line)
    print("Q/A JSONL GENERATOR (Ollama) — resilient, multi-QA, overlap, resume")
    print(line)
    print(f"Model:        {MODEL}")
    print(f"Input:        {INPUT_TXT}  ({total_chars:,} chars)")
    print(f"Output:       {OUTPUT_JSONL}")
    print(f"Bad outputs:  {BAD_OUTPUTS_FILE}")
    print(f"State:        {STATE_FILE}")
    print(f"Chunk size:   {CHUNK_SIZE} chars  (overlap {CHUNK_OVERLAP})")
    print(f"Chunks:       {total_chunks}")
    print(f"Q/A per chunk:{QA_PER_CHUNK}")
    if resume_from > 0:
        print(f"Resume:       skipping first {resume_from} chunk(s)")
    print(line)
    sys.stdout.flush()

def render_stats(
    idx: int,
    total: int,
    ok_items: int,
    bad_chunks: int,
    elapsed: float,
    last_dt: float,
    last_chunk_len: int,
    last_q: Optional[str],
    last_a: Optional[str],
    ema_s_per_chunk: Optional[float],
) -> None:
    done = idx
    left = total - done
    rate_avg = (done / elapsed) if elapsed > 0 else 0.0
    if ema_s_per_chunk and ema_s_per_chunk > 0:
        eta = left * ema_s_per_chunk
    else:
        eta = (left / rate_avg) if rate_avg > 0 else 0.0

    pct = (done / total) if total else 1.0
    w = term_width()
    line = "─" * min(w, 120)

    print(line)
    print(
        f"[{bar(pct, PROGRESS_BAR_WIDTH)}] "
        f"{done}/{total} ({pct*100:5.1f}%)  "
        f"ITEMS_OK:{ok_items}  BAD_CHUNKS:{bad_chunks}"
    )
    print(
        f"Elapsed: {fmt_td(elapsed)}  ETA: {fmt_td(eta)}  "
        f"Avg: {rate_avg:.2f} chunks/s  Last: {last_dt:.2f}s"
    )
    print(f"Last chunk: {last_chunk_len} chars")
    if SHOW_LAST_QA_PREVIEW and last_q and last_a:
        print(f"Q: {safe_preview(last_q)}")
        print(f"A: {safe_preview(last_a)}")
    sys.stdout.flush()

# ============================================================
# MAIN
# ============================================================

def main() -> None:
    # Load input
    if not os.path.exists(INPUT_TXT):
        print(f"Input file not found: {INPUT_TXT}", file=sys.stderr)
        sys.exit(1)

    with open(INPUT_TXT, "r", encoding="utf-8") as f:
        text = f.read()

    text = normalize_text(text)
    paragraphs = split_paragraphs(text)
    chunks = make_chunks(paragraphs)

    total_chars = len(text)
    total_chunks = len(chunks)
    if total_chunks == 0:
        print("No text / no chunks to process.")
        return

    # Resume logic
    state = load_state()
    resume_from = int(state.get("last_chunk_done", 0))
    # If output exists but state is missing, try a safe heuristic:
    # do not guess chunk->line mapping (because we now write multiple lines per chunk),
    # so state is the authority. If state missing, resume_from=0.
    if resume_from < 0:
        resume_from = 0
    if resume_from > total_chunks:
        resume_from = 0

    print_header(total_chars, total_chunks, resume_from)

    # Prepare bad log
    bad_out = open(BAD_OUTPUTS_FILE, "a", encoding="utf-8")  # append (so resume keeps history)

    # Dedup memory
    seen = set()

    # If resuming, preload seen keys from existing JSONL (optional but helps reduce duplicates)
    if DEDUP and os.path.exists(OUTPUT_JSONL):
        try:
            with open(OUTPUT_JSONL, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        obj = json.loads(line)
                        if isinstance(obj, dict) and "question" in obj and "answer" in obj:
                            seen.add(stable_key(obj["question"], obj["answer"]))
                    except Exception:
                        continue
        except Exception:
            pass

    # Stats
    t0 = time.time()
    ok_items = int(state.get("ok_items", 0))
    bad_chunks = int(state.get("bad_chunks", 0))
    total_ollama_time = float(state.get("total_ollama_time", 0.0))
    ema_s_per_chunk = state.get("ema_s_per_chunk", None)
    ema_s_per_chunk = float(ema_s_per_chunk) if ema_s_per_chunk is not None else None
    alpha = 0.18

    last_q = None
    last_a = None

    # Open output JSONL (append on resume, overwrite on fresh)
    out_mode = "a" if (resume_from > 0 and os.path.exists(OUTPUT_JSONL)) else "w"
    with open(OUTPUT_JSONL, out_mode, encoding="utf-8") as out:
        try:
            for i in range(resume_from, total_chunks):
                chunk_index = i + 1
                chunk = chunks[i]

                # Build prompt
                prompt = build_prompt(chunk, QA_PER_CHUNK)

                # Retry loop
                attempt = 0
                final_items: Optional[List[Dict[str, str]]] = None
                final_stdout = ""
                final_stderr = ""
                final_rc = 0
                final_dt = 0.0
                parse_err = None

                while attempt < MAX_RETRIES and final_items is None:
                    attempt += 1

                    stdout, stderr, rc, dt = call_ollama(prompt)
                    total_ollama_time += dt
                    final_stdout, final_stderr, final_rc, final_dt = stdout, stderr, rc, dt

                    # Update EMA (per chunk)
                    if ema_s_per_chunk is None:
                        ema_s_per_chunk = dt
                    else:
                        ema_s_per_chunk = alpha * dt + (1 - alpha) * ema_s_per_chunk

                    items, err = parse_qa_items(stdout)
                    parse_err = err

                    # If invalid and enabled, attempt repair once per attempt
                    if (rc == 0) and (items is None) and REPAIR_ATTEMPT:
                        rep_prompt = build_repair_prompt(stdout)
                        r_stdout, r_stderr, r_rc, r_dt = call_ollama(rep_prompt)
                        total_ollama_time += r_dt
                        final_stdout, final_stderr, final_rc, final_dt = r_stdout, (stderr + "\n" + r_stderr).strip(), r_rc, (dt + r_dt)

                        items2, err2 = parse_qa_items(r_stdout)
                        if items2 is not None:
                            items = items2
                            parse_err = None
                        else:
                            parse_err = err2 or parse_err

                    # Validate count: if model returned fewer items, accept (better than dropping),
                    # but we will keep trying a couple times to reach QA_PER_CHUNK.
                    if items is not None:
                        final_items = items
                        break

                    # Backoff before retry
                    sleep_s = (RETRY_BACKOFF_BASE ** (attempt - 1))
                    time.sleep(min(10.0, sleep_s))

                # If still invalid: log + continue
                if final_items is None or final_rc != 0:
                    bad_chunks += 1
                    bad_out.write("========================================\n")
                    bad_out.write(f"Chunk #{chunk_index}/{total_chunks}  len={len(chunk)}  rc={final_rc}  dt={final_dt:.2f}s  attempts={attempt}\n")
                    if final_stderr:
                        bad_out.write("---- STDERR ----\n")
                        bad_out.write(final_stderr + "\n")
                    bad_out.write("---- STDOUT ----\n")
                    bad_out.write(final_stdout + "\n")
                    if parse_err:
                        bad_out.write("---- PARSE ERROR ----\n")
                        bad_out.write(parse_err + "\n")
                    bad_out.write("\n")
                    bad_out.flush()

                    elapsed = time.time() - t0
                    render_stats(
                        idx=chunk_index,
                        total=total_chunks,
                        ok_items=ok_items,
                        bad_chunks=bad_chunks,
                        elapsed=elapsed,
                        last_dt=final_dt,
                        last_chunk_len=len(chunk),
                        last_q=last_q,
                        last_a=last_a,
                        ema_s_per_chunk=ema_s_per_chunk,
                    )
                    print("⚠️ Skipped invalid chunk output (see entrenamiento.bad.txt)")
                    # Update state
                    state.update({
                        "last_chunk_done": chunk_index,
                        "ok_items": ok_items,
                        "bad_chunks": bad_chunks,
                        "total_ollama_time": total_ollama_time,
                        "ema_s_per_chunk": ema_s_per_chunk,
                    })
                    save_state(state)
                    continue

                # Write items with dedup
                wrote = 0
                for it in final_items:
                    q = it["question"].strip()
                    a = it["answer"].strip()
                    if DEDUP:
                        key = stable_key(q, a)
                        if key in seen:
                            continue
                        seen.add(key)

                    out.write(jdump({"question": q, "answer": a}) + "\n")
                    wrote += 1
                    ok_items += 1
                    last_q, last_a = q, a

                out.flush()

                # Update console stats
                elapsed = time.time() - t0
                render_stats(
                    idx=chunk_index,
                    total=total_chunks,
                    ok_items=ok_items,
                    bad_chunks=bad_chunks,
                    elapsed=elapsed,
                    last_dt=final_dt,
                    last_chunk_len=len(chunk),
                    last_q=last_q,
                    last_a=last_a,
                    ema_s_per_chunk=ema_s_per_chunk,
                )
                if wrote == 0:
                    print("ℹ️ No new items written (all duplicates or empty).")

                # Persist state after each chunk
                state.update({
                    "last_chunk_done": chunk_index,
                    "ok_items": ok_items,
                    "bad_chunks": bad_chunks,
                    "total_ollama_time": total_ollama_time,
                    "ema_s_per_chunk": ema_s_per_chunk,
                })
                save_state(state)

        except KeyboardInterrupt:
            print("\nInterrupted. State saved. You can rerun to resume.")
        finally:
            bad_out.close()

    # Final summary
    elapsed = time.time() - t0
    w = term_width()
    line = "═" * min(w, 120)
    print(line)
    print("DONE")
    print(line)
    print(f"Chunks total:       {total_chunks}")
    print(f"Items written:      {ok_items}")
    print(f"Bad chunks skipped: {bad_chunks}")
    print(f"Total elapsed:      {fmt_td(elapsed)}")
    avg_dt = (total_ollama_time / max(1, total_chunks)) if total_chunks else 0.0
    print(f"Ollama avg/chunk:   {avg_dt:.2f}s")
    print(f"Output file:        {OUTPUT_JSONL}")
    if bad_chunks:
        print(f"Invalid details:    {BAD_OUTPUTS_FILE}")
    print(f"Resume state:       {STATE_FILE}")
    print(line)

if __name__ == "__main__":
    main()
