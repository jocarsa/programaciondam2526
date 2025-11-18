menu = []

while True:
  comida = input("Introduce el nombre de la comida: ")
  menu.append(comida)
  print("Tu comida hasta el momento es:")
  for elemento in menu:
    print(elemento)
