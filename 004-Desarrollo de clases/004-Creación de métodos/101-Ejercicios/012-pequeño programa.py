class Cliente():
  # Este es el método constructor
  def __init__(self):
    self.nombrecompleto = ""
    self.email = ""
  # Estos son los setters y los getters
  def setNombreCompleto(self,nuevonombre):
    self.nombrecompleto = nuevonombre
  def setEmail(self,nuevoemail):
    self.email = nuevoemail
  def getNombreCompleto(self):
    return self.nombrecompleto
  def getEmail(self):
    return self.email
    
# CRUD - Create, Read, Update, Delete
# CRUD SQL - INSERT, SELECT, UPDATE, DELETE

print("Gestor de clientes v0.1 Jose Vicente Carratala")
print("Selecciona una opción:")
print("1.-Insertar un nuevo cliente")
print("2.-Obtener listado de clientes")
opcion = int(input("Indica tu opción (1,2): "))

if opcion == 1:
  print("Voy a insertar un cliente")
elif opcion == 2:
  print("Saco el listado de clientes")
  
  

    

    


    
