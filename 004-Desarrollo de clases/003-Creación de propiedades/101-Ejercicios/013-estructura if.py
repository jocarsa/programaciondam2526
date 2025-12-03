'''
  Aplicación de gestión de productos
  (c) 2025 Jose Vicente Carratala
  Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
  def __init__(self):
    self.nombre = ""
    self.precio = 0
    
# Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v0.1 Jose Vicente Carratala")
# Le mostramos al usuario las opciones que tiene
print("Selecciona una opción:")
print("1.-Crear un nuevo producto")
print("2.-Listar productos")
print("3.-Actualizar productos")
print("4.-Eliminar productos")
opcion = int(input("Escoge tu opción: "))
# En función de la opción que coja el usuario
if opcion == 1:
  # O bien creamos un nuevo producto
  print("Creamos un nuevo producto")
elif opcion == 2:
  # O bien listamos los productos
  print("Vamos a listar los productos")
elif opcion == 3:
  # O bien actualizamos los productos
  print("Vamos a actualizar productos")
elif opcion == 4:
  # O bien eliminamos los productos
  print("Vamos a eliminar productos")
# Y volvemos a repetir
    

