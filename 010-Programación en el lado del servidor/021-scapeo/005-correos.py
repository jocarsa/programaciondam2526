import sqlite3
import json

DB_FILE = "webdata.sqlite"
OUTPUT_FILE = "emails.txt"

# Conectar a SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("SELECT emails_json FROM pages")

emails = set()

for (emails_json,) in cursor.fetchall():
    if not emails_json:
        continue

    try:
        lista = json.loads(emails_json)
        for email in lista:
            emails.add(email.lower().strip())
    except:
        pass


# Guardar TXT
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for email in sorted(emails):
        f.write(email + "\n")

conn.close()

print(f"Emails únicos exportados: {len(emails)}")
print(f"Archivo generado: {OUTPUT_FILE}")
