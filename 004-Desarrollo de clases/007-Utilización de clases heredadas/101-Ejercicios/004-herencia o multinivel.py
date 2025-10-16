class Entidad():
  def __init__(self):
    self.x = 0
    self.y = 0
    self.z = 0

class Animal(Entidad):
  def __init__(self):
    super().__init__()
    self.edad = 0
    self.nombre = ""
    self.raza = ""

class Gato(Animal):
  def __init__(self):
    super().__init__()    # Me traigo todo lo que tenga la clase superior

    
class Perro(Animal):      
  def __init__(self):
    super().__init__()  # Me traigo todo lo que tenga la clase superior
    

class Roca(Entidad):
  def __init__(self):
    super().__init__()


gato1 = Gato()
print(gato1.edad)

perro1 = Perro()
print(perro1.edad)
    
