import mysql.connector

print("Bienvenidos a la aplicacion")

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioceac",
  password="portafolioceac",
  database="portafolioceac"
  )
cursor = conexion.cursor()

while True:
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualiar registro")
  print("4.-Eliminar registro")

  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripcion: ")
    imagen = input("Introduce la imagen: ")
    url = input("Introduce la url: ")
    id_categoria = input("Introduce la categoria: ")
    cursor.execute('''
      INSERT INTO Piezas VALUES (
      NULL,
      "'''+titulo+'''",
      "'''+descripcion+'''",
      "'''+imagen+'''",
      "'''+url+'''",
      '''+id_categoria+'''
      );
    ''')
    conexion.commit()
  elif opcion == 2:

    cursor.execute('''
      SELECT * FROM Piezas;
    ''')

    filas = cursor.fetchall()

    for fila in filas:
      print(fila)
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
