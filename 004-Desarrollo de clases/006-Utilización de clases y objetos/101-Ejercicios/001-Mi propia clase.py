class Matematicas():
  def __init__(self):
    self.PI = 3.14159265359
    
  def redondeo(self,numero):
    entero = int(numero)
    decimal = numero - entero
    if decimal < 0.5:
      redondeo = 0
    else:
      redondeo = 1
    return entero + redondeo
    
Mate = Matematicas()
print(Mate.redondeo(4.7))
print(Mate.redondeo(4.2))
