# CRUD
# Create 
# Read
# Update
# Delete

print("Programa de gestión de clientes v0.1 Jose Vicente Carratala")

# Muestro opciones en el menú para el usuario
print("Selecciona una opción: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")

clientes = []   # Creo una lista VACIA

while True: # Esto desata un bucle infinito pero controlado

  # Le permito escoger una opción
  opcion = input("Escoge una opción: ")
  opcion = int(opcion)   # Convierto a entero
  
  if opcion == 1:
    print("Vamos a insertar un cliente")
    nuevocliente = input("Introduce el nombre del cliente: ")
    clientes.append(nuevocliente)
  elif opcion == 2:
    print("Vamos a ver los clientes")
    print(clientes)
  elif opcion == 3:
    print("Vamos a actualizar un cliente")
  elif opcion == 4:
    print("Vamos a eliminar un cliente")
  else:
    break
    
