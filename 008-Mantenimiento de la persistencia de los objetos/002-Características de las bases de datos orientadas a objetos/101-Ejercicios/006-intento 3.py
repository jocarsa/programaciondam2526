# save_rendered_html.py
# pip install playwright
# playwright install chromium
# python3 -m playwright install chromium

from pathlib import Path
from playwright.sync_api import sync_playwright

# =========================
# CONFIG (EDIT HERE)
# =========================
URL = "https://www.fotocasa.es/es/comprar/viviendas/valencia-capital/todas-las-zonas/l"          # target page
OUTPUT_HTML = "guardado.html"            # where to save rendered HTML
WAIT_SELECTOR = "body"               # CSS selector that indicates page is ready ("" to disable)
EXTRA_WAIT_MS = 2000                 # extra wait for late JS (0 to disable)
TIMEOUT_MS = 45000                   # navigation / wait timeout
SCREENSHOT_PATH = ""                 # e.g. "page.png" or "" to disable
HEADFUL = False                      # True = show browser window (debug)

# Chrome-like User-Agent (Linux)
CHROME_UA_LINUX = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not HEADFUL)

        context = browser.new_context(
            user_agent=CHROME_UA_LINUX,
            viewport={"width": 1366, "height": 768},
            locale="en-US",
            timezone_id="Europe/Madrid",
        )

        page = context.new_page()

        # Load page like a real browser and wait for JS/network to settle
        page.goto(URL, wait_until="networkidle", timeout=TIMEOUT_MS)

        # Optional: wait for a specific DOM element
        if WAIT_SELECTOR:
            page.wait_for_selector(WAIT_SELECTOR, timeout=TIMEOUT_MS)

        # Optional: extra delay for late hydration/widgets
        if EXTRA_WAIT_MS > 0:
            page.wait_for_timeout(EXTRA_WAIT_MS)

        # Get final rendered HTML (after JS execution)
        html = page.content()
        Path(OUTPUT_HTML).write_text(html, encoding="utf-8")

        # Optional screenshot for verification
        if SCREENSHOT_PATH:
            page.screenshot(path=SCREENSHOT_PATH, full_page=True)

        context.close()
        browser.close()

    print(f"Rendered HTML saved to: {OUTPUT_HTML}")

if __name__ == "__main__":
    main()
