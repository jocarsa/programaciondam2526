class Persona():
  def __init__(self,nombre,apellidos,email,direccion):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    self.direccion = direccion
  def dameDatos(self):
    return self.nombre+self.apellidos

class Profesor(Persona):
  def __init__(self,nombre,apellidos,email,direccion):
  	super().__init__(nombre, apellidos, email,direccion)
  
class Alumno(Persona):
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos, email,direccion)

class AlumnoOnline(Alumno):
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos, email,direccion)

class AlumnoPresencial(Alumno):
  def __init__(self,nombre,apellidos,email,direccion):
    super().__init__(nombre, apellidos, email,direccion)
    
alumno1 = Alumno("Jose Vicente","Carratala","info@jocarsa.com","Direccion")
print(alumno1.dameDatos())

profesor1 = Profesor("Juan","Garcia","juan@jocarsa.com","Direccion")
print(profesor1.dameDatos())