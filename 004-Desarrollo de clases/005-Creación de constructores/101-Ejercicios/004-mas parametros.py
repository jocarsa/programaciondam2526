class Gato():
  def __init__(self,edad,nombre):    # El constructor se ejecuta sí o sí
    self.edad = edad
    self.nombre = nombre
    
  def maulla(self):     # El resto de métodos sólo se ejecutan si los llamas
    return "El gato está maullando"
    
    
gato1 = Gato(5,"micifu")

    
