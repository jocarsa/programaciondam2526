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
# CONFIG (MAX SQUEEZE, STABLE)
# ============================================================

MODEL = "qwen2.5:3b-instruct"
INPUT_TXT = "convertido.txt"
OUTPUT_JSONL = "entrenamiento.jsonl"

# Aggressive extraction (still heavy)
QA_PER_CHUNK = 12
OVERASK_FACTOR = 2.0          # reduced from 2.5 to lower timeout risk
PASSES_PER_CHUNK = 5          # reduced from 6 to lower timeout risk

# Chunking tuned for coverage
CHUNK_SIZE = 1100
CHUNK_OVERLAP = 340
MIN_CHUNK = 450
MAX_CHUNK = 2200

TARGET_ITEMS_PER_CHUNK = max(1, int(QA_PER_CHUNK * OVERASK_FACTOR))

# Resilience
MAX_RETRIES = 4
RETRY_BACKOFF_BASE = 1.6
OLLAMA_TIMEOUT = 600          # increased (avoid TimeoutExpired)
REPAIR_ATTEMPT = True
MAX_OUTPUT_ITEMS_PER_CALL = 60

# Coverage enhancements
ENABLE_GAP_FILL_PASS = True
GAP_FILL_MIN_UNIQUE = max(6, QA_PER_CHUNK // 2)

# Fallback squeeze
ENABLE_MICRO_CHUNK_FALLBACK = True
MICRO_CHUNK_SIZE = 900
MICRO_CHUNK_OVERLAP = 180
MICRO_CHUNK_MAX_TRIES = 2

# Quality
DEDUP = True
NORMALIZE_WHITESPACE = True

# Files
BAD_OUTPUTS_FILE = "entrenamiento.bad.txt"
STATE_FILE = "entrenamiento.state.json"

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
        return (s or "").strip()
    s = (s or "").replace("\r\n", "\n").replace("\r", "\n")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def jdump(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False)

def canon(s: str) -> str:
    s = (s or "").lower()
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"[“”\"'`´]", "", s)
    s = re.sub(r"[,:;()\[\]{}]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def stable_key(q: str, a: str) -> str:
    return canon(q)[:260] + "||" + canon(a)[:520]

def uniq_count(items: List[Dict[str, str]]) -> int:
    s = set()
    for it in items:
        s.add(stable_key(it.get("question", ""), it.get("answer", "")))
    return len(s)

def _to_str(x: Any) -> str:
    if x is None:
        return ""
    if isinstance(x, bytes):
        return x.decode("utf-8", errors="replace")
    return str(x)


# ============================================================
# CHUNKING (paragraph-aware + overlap + sentence-friendly tail)
# ============================================================

def split_paragraphs(text: str) -> List[str]:
    text = normalize_text(text)
    if not text:
        return []
    parts = re.split(r"\n\s*\n", text)
    return [p.strip() for p in parts if p.strip()]

def smart_tail(prev: str, max_chars: int) -> str:
    prev = prev or ""
    tail = prev[-max_chars:]
    matches = list(re.finditer(r"([.!?]|\.{3})\s+", tail))
    if matches:
        last = matches[-1]
        cut = last.end()
        if 0 < cut < len(tail):
            return tail[cut:].strip()
    return tail.strip()

def make_chunks(paragraphs: List[str],
                chunk_size: int,
                chunk_overlap: int,
                min_chunk: int,
                max_chunk: int) -> List[str]:
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

        if len(p) > max_chunk:
            flush()
            start = 0
            while start < len(p):
                end = min(len(p), start + max_chunk)
                sub = p[start:end].strip()
                if sub:
                    chunks.append(sub)
                start = end
            continue

        if (buf_len + len(p) + (2 if buf else 0) <= chunk_size) or (buf_len < min_chunk):
            buf.append(p)
            buf_len += len(p) + (2 if buf_len else 0)
        else:
            flush()
            buf.append(p)
            buf_len = len(p)

    flush()

    if chunk_overlap > 0 and len(chunks) > 1:
        overlapped: List[str] = [chunks[0]]
        for i in range(1, len(chunks)):
            prev = overlapped[-1]
            tail = smart_tail(prev, chunk_overlap)
            merged = (tail + "\n\n" + chunks[i]).strip() if tail else chunks[i].strip()
            overlapped.append(merged)
        chunks = overlapped

    return chunks


# ============================================================
# OLLAMA CALLS (FIXED: bytes-safe + timeout-safe)
# ============================================================

def call_ollama(prompt: str) -> Tuple[str, str, int, float]:
    """
    Returns: (stdout, stderr, returncode, elapsed_seconds)
    Always returns stdout/stderr as str (never bytes).
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
        out = _to_str(getattr(e, "stdout", "")).strip()
        err = _to_str(getattr(e, "stderr", "")).strip()
        err = (err + "\nTIMEOUT").strip() if err else "TIMEOUT"
        return (out, err, 124, dt)

    except Exception as e:
        dt = time.time() - t0
        return ("", f"EXCEPTION: {e}", 125, dt)


# ============================================================
# ROBUST JSON EXTRACTION / VALIDATION
# ============================================================

def strip_code_fences(s: str) -> str:
    s = (s or "").strip()
    s = re.sub(r"^\s*```(?:json)?\s*", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\s*```\s*$", "", s)
    return s.strip()

def find_balanced_json_candidates(s: str) -> List[str]:
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

    scan("[", "]")
    scan("{", "}")

    seen = set()
    out: List[str] = []
    for c in candidates:
        c2 = c.strip()
        if c2 and c2 not in seen:
            seen.add(c2)
            out.append(c2)
    return out

def normalize_items(obj: Any) -> Optional[List[Dict[str, str]]]:
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
                if len(q) < 10 or len(a) < 10:
                    continue
                items.append({"question": q, "answer": a})

    if not items:
        return None

    if len(items) > MAX_OUTPUT_ITEMS_PER_CALL:
        items = items[:MAX_OUTPUT_ITEMS_PER_CALL]

    return items

def parse_qa_items(raw: str) -> Tuple[Optional[List[Dict[str, str]]], Optional[str]]:
    raw = strip_code_fences(raw)

    try:
        obj = json.loads(raw)
        items = normalize_items(obj)
        if items is not None:
            return items, None
    except Exception:
        pass

    for cand in find_balanced_json_candidates(raw):
        try:
            obj = json.loads(cand)
            items = normalize_items(obj)
            if items is not None:
                return items, None
        except Exception:
            continue

    return None, "Could not parse valid JSON with required fields"


# ============================================================
# PROMPTS (multi-pass, targeted)  ✅ BRACES ESCAPED
# ============================================================

BASE_RULES = """
Eres un generador de dataset de entrenamiento para un LLM.
Tu tarea: extraer INFORMACIÓN del texto y convertirla en preguntas/respuestas (Q/A) muy específicas.

REGLAS IMPORTANTES:
- Responde SIEMPRE en español.
- SOLO usa información explícita del texto. NO inventes datos. NO añadas contexto externo.
- Cada respuesta debe poder justificarse con el texto (sin suposiciones).
- Evita preguntas vagas o genéricas. Cada pregunta debe incluir detalles concretos del texto (términos, condiciones, pasos, valores, restricciones).
- Prioriza hechos, definiciones, pasos, requisitos, excepciones, listas, ejemplos y matices.
- No repitas la misma idea con palabras distintas.
"""

FORMAT_RULES = """
FORMATO DE SALIDA (JSON ESTRICTO, sin texto adicional):
Devuelve un ARRAY JSON con EXACTAMENTE {n_items} elementos.
Cada elemento: {{"question":"...","answer":"..."}}
No incluyas claves extra. No incluyas markdown. No incluyas comentarios.
"""

PASS_INSTRUCTIONS = [
    "ENFOQUE: Hechos, definiciones, términos, conceptos clave. Extrae lo máximo posible.",
    "ENFOQUE: Procedimientos, pasos, secuencias, instrucciones, algoritmos descritos en el texto.",
    "ENFOQUE: Restricciones, condiciones, requisitos, excepciones, advertencias, casos límite.",
    "ENFOQUE: Listas, clasificaciones, comparaciones, tablas implícitas (elemento -> descripción).",
    "ENFOQUE: Ejemplos concretos del texto y qué ilustran (caso -> conclusión).",
]

def build_prompt(chunk: str, n_items: int, pass_idx: int) -> str:
    focus = PASS_INSTRUCTIONS[min(pass_idx, len(PASS_INSTRUCTIONS)-1)]
    return f"""
{BASE_RULES}

{focus}

{FORMAT_RULES.format(n_items=n_items)}

TEXTO:
\"\"\"
{chunk}
\"\"\"
""".strip()

def build_gap_fill_prompt(chunk: str, existing_json: str, n_items: int) -> str:
    return f"""
{BASE_RULES}

ENFOQUE: Rellenar HUECOS de cobertura.
A continuación tienes Q/A ya extraídas. NO repitas ideas ya cubiertas.
Genera nuevas Q/A sobre información distinta del texto (detalles no usados aún).
Si una idea ya está cubierta, NO la reformules: busca otra.

Q/A existentes:
\"\"\"
{existing_json}
\"\"\"

{FORMAT_RULES.format(n_items=n_items)}

TEXTO:
\"\"\"
{chunk}
\"\"\"
""".strip()

def build_repair_prompt(bad_output: str) -> str:
    return f"""
Convierte el contenido siguiente en JSON ESTRICTO únicamente.
Devuelve SOLO:
- Un objeto {{"question":"...","answer":"..."}}
- O un array de objetos con esas claves.
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


# ============================================================
# CONSOLE
# ============================================================

def print_header(total_chars: int, total_chunks: int, resume_from: int) -> None:
    w = term_width()
    line = "─" * min(w, 120)
    print(line)
    print("Q/A JSONL GENERATOR (Ollama) — MAX SQUEEZE (multi-pass + over-ask + gap-fill + fallback)")
    print(line)
    print(f"Model:        {MODEL}")
    print(f"Input:        {INPUT_TXT}  ({total_chars:,} chars)")
    print(f"Output:       {OUTPUT_JSONL}")
    print(f"Bad outputs:  {BAD_OUTPUTS_FILE}")
    print(f"State:        {STATE_FILE}")
    print(f"Chunk size:   {CHUNK_SIZE} chars  (overlap {CHUNK_OVERLAP})")
    print(f"Chunks:       {total_chunks}")
    print(f"Keep/chunk:   {QA_PER_CHUNK}   Ask/pass: {TARGET_ITEMS_PER_CHUNK}   Passes: {PASSES_PER_CHUNK}")
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
# CORE EXTRACTION
# ============================================================

def run_prompt_with_retries(
    prompt: str,
    bad_out,
    chunk_index: int,
    total_chunks: int,
    chunk_len: int
) -> Tuple[Optional[List[Dict[str, str]]], str, str, int, float, Optional[str]]:

    attempt = 0
    final_stdout = ""
    final_stderr = ""
    final_rc = 0
    final_dt = 0.0
    parse_err = None
    final_items: Optional[List[Dict[str, str]]] = None

    while attempt < MAX_RETRIES and final_items is None:
        attempt += 1
        stdout, stderr, rc, dt = call_ollama(prompt)
        final_stdout, final_stderr, final_rc, final_dt = stdout, stderr, rc, dt

        # timeout => do not crash, just backoff and retry
        if rc == 124:
            time.sleep(min(10.0, 1.5 * attempt))
            continue

        items, err = parse_qa_items(stdout)
        parse_err = err

        if (rc == 0) and (items is None) and REPAIR_ATTEMPT:
            rep_prompt = build_repair_prompt(stdout)
            r_stdout, r_stderr, r_rc, r_dt = call_ollama(rep_prompt)
            final_stdout = r_stdout
            final_stderr = (stderr + "\n" + r_stderr).strip()
            final_rc = r_rc
            final_dt = dt + r_dt

            if r_rc == 124:
                time.sleep(min(10.0, 1.5 * attempt))
                continue

            items2, err2 = parse_qa_items(r_stdout)
            if items2 is not None:
                items = items2
                parse_err = None
            else:
                parse_err = err2 or parse_err

        if items is not None and final_rc == 0:
            final_items = items
            break

        sleep_s = (RETRY_BACKOFF_BASE ** (attempt - 1))
        time.sleep(min(10.0, sleep_s))

    if final_items is None:
        bad_out.write("========================================\n")
        bad_out.write(
            f"Chunk #{chunk_index}/{total_chunks}  len={chunk_len}  "
            f"rc={final_rc}  dt={final_dt:.2f}s  attempts={attempt}\n"
        )
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

    return final_items, final_stdout, final_stderr, final_rc, final_dt, parse_err

def trim_and_rank(items: List[Dict[str, str]], keep: int) -> List[Dict[str, str]]:
    def score(it: Dict[str, str]) -> int:
        q = it.get("question", "")
        a = it.get("answer", "")
        bonus = 0
        if re.search(r"\d", q + " " + a):
            bonus += 12
        if re.search(r"\b(si|cuando|siempre que|salvo|excepto|requisit|condici|paso|procedim|lista|por ejemplo|umbral|rango)\b",
                     (q + " " + a).lower()):
            bonus += 8
        return len(q) + len(a) + bonus

    items_sorted = sorted(items, key=score, reverse=True)
    return items_sorted[:keep]

def merge_dedup(items: List[Dict[str, str]], seen: set) -> List[Dict[str, str]]:
    out: List[Dict[str, str]] = []
    for it in items:
        q = it["question"].strip()
        a = it["answer"].strip()
        key = stable_key(q, a)
        if DEDUP and key in seen:
            continue
        if DEDUP:
            seen.add(key)
        out.append({"question": q, "answer": a})
    return out

def extract_max_from_chunk(
    chunk: str,
    seen: set,
    bad_out,
    chunk_index: int,
    total_chunks: int
) -> Tuple[Optional[List[Dict[str, str]]], float]:

    total_dt = 0.0
    collected: List[Dict[str, str]] = []
    any_fail = False

    for pidx in range(PASSES_PER_CHUNK):
        prompt = build_prompt(chunk, TARGET_ITEMS_PER_CHUNK, pidx)
        items, _, _, rc, dt, _ = run_prompt_with_retries(prompt, bad_out, chunk_index, total_chunks, len(chunk))
        total_dt += dt
        if items is None or rc != 0:
            any_fail = True
            continue
        collected.extend(items)

    # Dedup within-chunk
    tmp_seen = set()
    unique_collected: List[Dict[str, str]] = []
    for it in collected:
        k = stable_key(it.get("question", ""), it.get("answer", ""))
        if k in tmp_seen:
            continue
        tmp_seen.add(k)
        unique_collected.append(it)
    collected = unique_collected

    # Gap fill if weak coverage
    if ENABLE_GAP_FILL_PASS and uniq_count(collected) < GAP_FILL_MIN_UNIQUE:
        existing_json = jdump(collected[:min(len(collected), 12)])
        gap_prompt = build_gap_fill_prompt(chunk, existing_json, TARGET_ITEMS_PER_CHUNK)
        items, _, _, rc, dt, _ = run_prompt_with_retries(gap_prompt, bad_out, chunk_index, total_chunks, len(chunk))
        total_dt += dt
        if items is not None and rc == 0:
            collected.extend(items)

    # Micro-chunk fallback if still empty
    if (not collected) and ENABLE_MICRO_CHUNK_FALLBACK:
        paras = split_paragraphs(chunk)
        micro_chunks = make_chunks(paras, MICRO_CHUNK_SIZE, MICRO_CHUNK_OVERLAP, 200, MICRO_CHUNK_SIZE)
        tries = 0
        for mch in micro_chunks:
            if tries >= MICRO_CHUNK_MAX_TRIES:
                break
            tries += 1
            prompt = build_prompt(mch, TARGET_ITEMS_PER_CHUNK, 0)
            items, _, _, rc, dt, _ = run_prompt_with_retries(prompt, bad_out, chunk_index, total_chunks, len(mch))
            total_dt += dt
            if items is not None and rc == 0:
                collected.extend(items)

    if not collected and any_fail:
        return None, total_dt

    merged = merge_dedup(collected, seen)
    if not merged:
        return [], total_dt

    merged = trim_and_rank(merged, QA_PER_CHUNK)
    return merged, total_dt


# ============================================================
# MAIN
# ============================================================

def main() -> None:
    if not os.path.exists(INPUT_TXT):
        print(f"Input file not found: {INPUT_TXT}", file=sys.stderr)
        sys.exit(1)

    with open(INPUT_TXT, "r", encoding="utf-8") as f:
        text = normalize_text(f.read())

    paragraphs = split_paragraphs(text)
    chunks = make_chunks(paragraphs, CHUNK_SIZE, CHUNK_OVERLAP, MIN_CHUNK, MAX_CHUNK)

    total_chars = len(text)
    total_chunks = len(chunks)
    if total_chunks == 0:
        print("No text / no chunks to process.")
        return

    state = load_state()
    resume_from = int(state.get("last_chunk_done", 0))
    if resume_from < 0 or resume_from > total_chunks:
        resume_from = 0

    print_header(total_chars, total_chunks, resume_from)

    bad_out = open(BAD_OUTPUTS_FILE, "a", encoding="utf-8")

    # global dedup set
    seen = set()
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

    t0 = time.time()
    ok_items = int(state.get("ok_items", 0))
    bad_chunks = int(state.get("bad_chunks", 0))
    total_ollama_time = float(state.get("total_ollama_time", 0.0))
    ema_s_per_chunk = state.get("ema_s_per_chunk", None)
    ema_s_per_chunk = float(ema_s_per_chunk) if ema_s_per_chunk is not None else None
    alpha = 0.18

    last_q = None
    last_a = None

    out_mode = "a" if (resume_from > 0 and os.path.exists(OUTPUT_JSONL)) else "w"
    with open(OUTPUT_JSONL, out_mode, encoding="utf-8") as out:
        try:
            for i in range(resume_from, total_chunks):
                chunk_index = i + 1
                chunk = chunks[i]

                items, dt = extract_max_from_chunk(chunk, seen, bad_out, chunk_index, total_chunks)
                total_ollama_time += dt

                if ema_s_per_chunk is None:
                    ema_s_per_chunk = max(0.01, dt)
                else:
                    ema_s_per_chunk = alpha * max(0.01, dt) + (1 - alpha) * ema_s_per_chunk

                if items is None:
                    bad_chunks += 1
                    elapsed = time.time() - t0
                    render_stats(
                        idx=chunk_index,
                        total=total_chunks,
                        ok_items=ok_items,
                        bad_chunks=bad_chunks,
                        elapsed=elapsed,
                        last_dt=dt,
                        last_chunk_len=len(chunk),
                        last_q=last_q,
                        last_a=last_a,
                        ema_s_per_chunk=ema_s_per_chunk,
                    )
                    print("⚠️ Chunk failed after retries (see entrenamiento.bad.txt)")
                    state.update({
                        "last_chunk_done": chunk_index,
                        "ok_items": ok_items,
                        "bad_chunks": bad_chunks,
                        "total_ollama_time": total_ollama_time,
                        "ema_s_per_chunk": ema_s_per_chunk,
                    })
                    save_state(state)
                    continue

                wrote = 0
                for it in items:
                    q = it["question"]
                    a = it["answer"]
                    out.write(jdump({"question": q, "answer": a}) + "\n")
                    wrote += 1
                    ok_items += 1
                    last_q, last_a = q, a

                out.flush()

                elapsed = time.time() - t0
                render_stats(
                    idx=chunk_index,
                    total=total_chunks,
                    ok_items=ok_items,
                    bad_chunks=bad_chunks,
                    elapsed=elapsed,
                    last_dt=dt,
                    last_chunk_len=len(chunk),
                    last_q=last_q,
                    last_a=last_a,
                    ema_s_per_chunk=ema_s_per_chunk,
                )
                if wrote == 0:
                    print("ℹ️ No new items written (all duplicates/filtered).")

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

