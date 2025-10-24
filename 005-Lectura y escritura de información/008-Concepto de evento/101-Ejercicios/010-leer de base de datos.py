import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
  SELECT * FROM clientes;
''')

filas = cursor.fetchall()

for fila in filas:
  print(fila)
  
cursor.close()
conexion.close()
