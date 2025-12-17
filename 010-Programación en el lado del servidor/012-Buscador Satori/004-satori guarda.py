import requests									# Importamos requests
from lxml import html						# importamos HTML
import mysql.connector					# Importamos MySQL

URL = "https://elpais.com"

DB_HOST = "localhost"						
DB_USER = "satori"
DB_PASSWORD = "Satori123$"
DB_NAME = "satori"

response = requests.get(URL, timeout=10, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
})
response.raise_for_status()

tree = html.fromstring(response.content)

title_list = tree.xpath("//title/text()")										# Saco el titulo
web_title = title_list[0].strip() if title_list else None


html_content = response.text[:255] 															# HTML completo

print("WEB TITLE:")
print(web_title or "No title found")

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    charset="utf8mb4",
    use_unicode=True
)																													# Guardar a MySQL

try:
    cur = conn.cursor()

    sql = """
        INSERT INTO paginas (titulo, url, contenido)
        VALUES (%s, %s, %s)
    """
    cur.execute(sql, (web_title, URL, html_content))
    conn.commit()																				# Inserto

    print(f"\nOK: guardado en MySQL. ID insertado: {cur.lastrowid}")

finally:
    try:
        cur.close()
    except Exception:
        pass
    conn.close()
