# pip3 install mysql-connector-python --break-system-packages
# sudo apt install libmysqlclient-dev python3-mysql.connector
import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
  INSERT INTO clientes
  VALUES(
    NULL,
    "12345678Z",
    "Jose Vicente",
    "Carratala Sanchis",
    "info@jocarsa.com"
  );
''')
conexion.commit()
cursor.close()
conexion.close()
