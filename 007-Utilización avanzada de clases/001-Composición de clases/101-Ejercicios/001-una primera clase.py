class Alumno():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
alumno1 = Alumno("Jose Vicente","Carratala","info@jocarsa.com")
print(alumno1)