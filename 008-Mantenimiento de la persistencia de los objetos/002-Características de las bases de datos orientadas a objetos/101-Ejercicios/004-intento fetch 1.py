import requests
from pathlib import Path

def fetch_html(url: str, out_path: str = "page.html", timeout: int = 30) -> str:
    # Chrome-ish headers (not perfect, but good enough for many sites)
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    }

    session = requests.Session()
    session.headers.update(headers)

    r = session.get(url, timeout=timeout, allow_redirects=True)
    r.raise_for_status()

    Path(out_path).write_text(r.text, encoding="utf-8")
    return out_path

if __name__ == "__main__":
    url = "https://www.fotocasa.es/es/comprar/viviendas/valencia-capital/todas-las-zonas/l"
    out = fetch_html(url, "page.html")
    print(f"Saved to: {out}")
    
    
