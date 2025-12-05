class Profesor():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
  def dameDatos(self):
    return self.nombre+self.apellidos

class Alumno():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
  def dameDatos(self):
    return self.nombre+self.apellidos
    
alumno1 = Alumno("Jose Vicente","Carratala","info@jocarsa.com")
print(alumno1.dameDatos())

profesor1 = Profesor("Juan","Garcia","juan@jocarsa.com")
print(profesor1.dameDatos())