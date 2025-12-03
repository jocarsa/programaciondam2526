print("Lista de la compra v0.1")

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
  elif opcion == 2:
    print("Listamos los elementos de la lista:")
    print(lista_de_la_compra)
