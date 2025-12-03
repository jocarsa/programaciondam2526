class Gato():
  def __init__(self):    # El constructor se ejecuta sí o sí
    self.edad = 0
    
  def maulla(self):     # El resto de métodos sólo se ejecutan si los llamas
    return "El gato está maullando"
    
    
gato1 = Gato()
print(gato1.edad)
gato1.edad = 5
print(gato1.edad)

print(gato1.maulla())
    
