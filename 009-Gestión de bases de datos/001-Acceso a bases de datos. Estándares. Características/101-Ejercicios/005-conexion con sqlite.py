import sqlite3

# Conexión a la base de datos SQLite (archivo .db)
conn = sqlite3.connect("empresa2026.db")

# Opcional: obtener filas como diccionarios
# conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
for row in cursor.fetchall():
    print(row)

conn.close()
