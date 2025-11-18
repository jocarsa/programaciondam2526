menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva comida en el menú")
  print("2.-Listar comidas en el menú")
  opcion = input("Selecciona una opción:")
  comida = input("Introduce el nombre de la comida: ")
  menu.append(comida)
  print("Tu comida hasta el momento es:")
  for elemento in menu:
    print(elemento)
