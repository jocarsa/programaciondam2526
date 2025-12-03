class Gato():
  def __init__(self,edad):    # El constructor se ejecuta sí o sí
    self.edad = edad
    
  def maulla(self):     # El resto de métodos sólo se ejecutan si los llamas
    return "El gato está maullando"
    
    
gato1 = Gato(5)

    
