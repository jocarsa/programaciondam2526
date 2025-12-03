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
    
  def techo(self,numero):
    return int(numero)+1
  def suelo(self,numero):
    return int(numero)
    
Mate = Matematicas()
print(Mate.redondeo(4.7))
print(Mate.redondeo(4.2))
print(Mate.techo(4.7))
print(Mate.suelo(4.7))
