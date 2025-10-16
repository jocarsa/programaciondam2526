# Las propiedades son como las variables PERO dentro de una clase

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.edad = 0
    self.telefonos = []
    
# Ahora instancio un nuevo objeto
cliente1 = Cliente()

# Ahora le escribo una propiedad

cliente1.nombre = "Jose Vicente"

print("El nombre del cliente es:",cliente1.nombre)

cliente1.telefonos.append("63354333")
cliente1.telefonos.append("65436456")

print(cliente1.telefonos)
    

