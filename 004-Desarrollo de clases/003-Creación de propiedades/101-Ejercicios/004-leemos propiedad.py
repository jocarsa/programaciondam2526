# Las propiedades son como las variables PERO dentro de una clase

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.edad = 0
    self.telefonos = ['543534','5345345']
    
# Ahora instancio un nuevo objeto
cliente1 = Cliente()

# Ahora le escribo una propiedad

cliente1.nombre = "Jose Vicente"

print("El nombre del cliente es:",cliente1.nombre)
    

