import re
import time
import json
import sqlite3
from datetime import datetime

import requests
from lxml import html


# ----------------------------
# CONFIG
# ----------------------------
INPUT_FILE = "datos.csv"
SQLITE_FILE = "webdata.sqlite"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-r1:1.5b"

HTTP_TIMEOUT = 15
OLLAMA_TIMEOUT = 120

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"


# ----------------------------
# TEXT + EMAIL EXTRACTION
# ----------------------------
EMAIL_RE = re.compile(
    r"""(?ix)
    \b
    [a-z0-9._%+\-]+
    @
    [a-z0-9.\-]+
    \.
    [a-z]{2,}
    \b
    """
)

def normalize_text(s: str) -> str:
    s = re.sub(r"\s+", " ", s or "").strip()
    return s

def extract_title(tree) -> str:
    t = tree.xpath("//title/text()")
    return normalize_text(t[0]) if t else ""

def extract_visible_text(tree, max_chars: int = 20000) -> str:
    """
    Pragmatic "visible-ish" text extraction:
    - Remove script/style/noscript/svg
    - Collect text from common content tags
    - Fallback to body text
    """
    for bad in tree.xpath("//script|//style|//noscript|//svg"):
        bad.getparent().remove(bad)

    parts = []
    # Prefer typical content-bearing tags
    for xp in [
        "//main//*[self::p or self::li or self::h1 or self::h2 or self::h3 or self::h4]//text()",
        "//*[self::p or self::li or self::h1 or self::h2 or self::h3 or self::h4]//text()",
    ]:
        txt = tree.xpath(xp)
        if txt:
            parts = txt
            break

    if not parts:
        parts = tree.xpath("//body//text()")

    text = normalize_text(" ".join(parts))
    return text[:max_chars]

def extract_emails(tree, text: str) -> list[str]:
    emails = set()

    # Regex over extracted text
    for m in EMAIL_RE.findall(text or ""):
        emails.add(m.lower())

    # mailto links
    for href in tree.xpath("//a[starts-with(translate(@href,'MAILTO','mailto'),'mailto:')]/@href"):
        # mailto:someone@domain.tld?subject=...
        addr = href.split(":", 1)[1].split("?", 1)[0].strip()
        if addr and EMAIL_RE.fullmatch(addr):
            emails.add(addr.lower())

    return sorted(emails)


# ----------------------------
# OLLAMA SUMMARY
# ----------------------------
def summarize_with_ollama(page_text: str) -> str:
    prompt = f"""Resume en un solo párrafo en español de qué trata la siguiente página web:

{page_text[:4000]}
"""
    payload = {"model": MODEL, "prompt": prompt, "stream": False}
    r = requests.post(OLLAMA_URL, json=payload, timeout=OLLAMA_TIMEOUT)
    r.raise_for_status()
    data = r.json()
    return (data.get("response") or "").strip()


# ----------------------------
# SQLITE
# ----------------------------
def init_db(conn: sqlite3.Connection) -> None:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS pages (
        id            INTEGER PRIMARY KEY AUTOINCREMENT,
        url           TEXT NOT NULL UNIQUE,
        title         TEXT,
        summary       TEXT,
        emails_json   TEXT,
        http_status   INTEGER,
        fetched_at    TEXT,
        error         TEXT
    )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_pages_url ON pages(url)")
    conn.commit()

def upsert_page(conn: sqlite3.Connection, row: dict) -> None:
    conn.execute("""
    INSERT INTO pages (url, title, summary, emails_json, http_status, fetched_at, error)
    VALUES (:url, :title, :summary, :emails_json, :http_status, :fetched_at, :error)
    ON CONFLICT(url) DO UPDATE SET
        title       = excluded.title,
        summary     = excluded.summary,
        emails_json = excluded.emails_json,
        http_status = excluded.http_status,
        fetched_at  = excluded.fetched_at,
        error       = excluded.error
    """, row)
    conn.commit()


# ----------------------------
# MAIN
# ----------------------------
def main():
    # Read URLs (one per line)
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        urls = [ln.strip() for ln in f.readlines() if ln.strip()]

    conn = sqlite3.connect(SQLITE_FILE)
    init_db(conn)

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Procesando: {url}")

        fetched_at = datetime.utcnow().isoformat(timespec="seconds") + "Z"

        try:
            resp = session.get(url, timeout=HTTP_TIMEOUT, allow_redirects=True)
            status = resp.status_code

            tree = html.fromstring(resp.content)
            tree.make_links_absolute(resp.url)

            title = extract_title(tree)
            text = extract_visible_text(tree)
            if not text:
                raise RuntimeError("No se pudo extraer contenido textual.")

            emails = extract_emails(tree, text)

            summary = summarize_with_ollama(text)

            row = {
                "url": url,
                "title": title,
                "summary": summary,
                "emails_json": json.dumps(emails, ensure_ascii=False),
                "http_status": status,
                "fetched_at": fetched_at,
                "error": None,
            }
            upsert_page(conn, row)

            print(f"Título: {title[:120]}")
            print(f"Emails encontrados: {len(emails)}")
            if emails:
                print(" - " + "\n - ".join(emails[:10]) + ("" if len(emails) <= 10 else "\n - ..."))
            print("Resumen guardado en SQLite.")

        except Exception as e:
            row = {
                "url": url,
                "title": None,
                "summary": None,
                "emails_json": json.dumps([], ensure_ascii=False),
                "http_status": None,
                "fetched_at": fetched_at,
                "error": str(e),
            }
            upsert_page(conn, row)
            print(f"Error: {e}")

        # Optional: small polite delay to reduce load
        time.sleep(0.5)

    conn.close()
    print(f"\nOK. Base de datos creada/actualizada: {SQLITE_FILE}")


if __name__ == "__main__":
    main()