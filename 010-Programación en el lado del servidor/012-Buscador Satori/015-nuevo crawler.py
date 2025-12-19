import requests
from lxml import html
import mysql.connector
import time
from urllib.parse import urljoin, urlparse

URLS = ["https://www.ceac.es/"]

DB_HOST = "localhost"
DB_USER = "satori"
DB_PASSWORD = "Satori123$"
DB_NAME = "satori"

VISITADAS = set()  # Para evitar bucles infinitos


def sanitize_links(base_url, links):
    urls_validas = []

    for link in links:
        if not link:
            continue

        link = link.strip()

        # Ignorar enlaces basura
        if link.startswith(("#", "javascript:", "mailto:", "tel:")):
            continue

        # Convertir relativos en absolutos
        full_url = urljoin(base_url, link)

        parsed = urlparse(full_url)

        # Solo http/https
        if parsed.scheme not in ("http", "https"):
            continue

        # Evitar URLs absurdamente largas
        if len(full_url) > 500:
            continue

        urls_validas.append(full_url)

    return list(set(urls_validas))  # eliminar duplicados


def extrae_meta_description(tree):
    # Cubre: name="description", NAME="DESCRIPTION", property="og:description", etc.
    desc = tree.xpath(
        "string(//meta[translate(@name,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='description']/@content)"
    ).strip()

    if not desc:
        desc = tree.xpath(
            "string(//meta[translate(@property,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='og:description']/@content)"
        ).strip()

    return desc or None


def busca(URLS):
    for URL in URLS:

        if URL in VISITADAS:
            continue

        VISITADAS.add(URL)

        time.sleep(5)

        try:
            print("Procesando:", URL)

            response = requests.get(
                URL,
                timeout=10,
                headers={
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
                }
            )
            response.raise_for_status()

            tree = html.fromstring(response.content)

            title_list = tree.xpath("//title/text()")
            web_title = title_list[0].strip() if title_list else None

            # NUEVO: meta description
            web_description = extrae_meta_description(tree)

            # Contenido (ajusta el corte si quieres guardar más/menos)
            html_content = response.text[:5000]

            print("WEB TITLE:")
            print(web_title or "No title found")
            print("META DESCRIPTION:")
            print(web_description or "No description found")

            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                charset="utf8mb4",
                use_unicode=True
            )

            try:
                cur = conn.cursor()

                sql = """
                    INSERT INTO paginas (titulo, descripcion, url, contenido)
                    VALUES (%s, %s, %s, %s)
                """
                cur.execute(sql, (web_title, web_description, URL, html_content))
                conn.commit()

                print(f"OK MySQL → ID: {cur.lastrowid}")

            finally:
                try:
                    cur.close()
                except Exception:
                    pass
                conn.close()

            enlaces = tree.xpath("//a/@href")
            enlaces_limpios = sanitize_links(URL, enlaces)

            busca(enlaces_limpios)

        except Exception as e:
            print("Error pero continuamos:", e)


busca(URLS)
