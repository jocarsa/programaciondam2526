import requests
from pathlib import Path

def fetch_json(api_url: str, out_path: str = "data.json"):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.fotocasa.es/es/comprar/viviendas/valencia-capital/todas-las-zonas/l",
        "Origin": "https://www.fotocasa.es/es/comprar/viviendas/valencia-capital/todas-las-zonas/l",
    }

    r = requests.get(api_url, headers=headers, timeout=30)
    r.raise_for_status()
    Path(out_path).write_text(r.text, encoding="utf-8")
    return out_path
