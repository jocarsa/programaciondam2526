print("Lista de la compra v0.1")
import json                   # Para usar la libreria tengo que importarla

lista_de_la_compra = []

while True:
  print("Selecciona una opcion")
  print("1.-Añadir elemento a la lista")
  print("2.-Leer la lista")
  opcion = int(input("Tu opción: "))
  
  if opcion == 1:
    print("Añadimos un elemento a la lista:")
    nombre = input("Indica el nombre del producto: ")
    cantidad = input("Indica la cantidad del producto: ")
    lista_de_la_compra.append({"nombre":nombre,"cantidad":cantidad})
    archivo = open("lista.json","w")         # Abro el archivo
    json.dump(lista_de_la_compra,archivo)    # Guardo en json
    archivo.close()                          # Cierro el archivo
  elif opcion == 2:
    print("Listamos los elementos de la lista:")
    for producto in lista_de_la_compra:
      print("Producto:",producto['nombre'])
      print("Cantidad:",producto['cantidad'])
      print("##############################") # Esto es estético, separador
