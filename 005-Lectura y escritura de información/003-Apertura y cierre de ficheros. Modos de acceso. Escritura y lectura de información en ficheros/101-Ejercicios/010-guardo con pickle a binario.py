import pickle

class Cliente():
  def __init__(self,nuevonombre,nuevoemail):
    self.nombre = nuevonombre
    self.email = nuevoemail

clientes = []

clientes.append(Cliente("Jose Vicente","info@jocarsa.com"))
clientes.append(Cliente("Juan","juan@jocarsa.com"))

archivo = open("clientes.bin","wb")
pickle.dump(clientes,archivo)
archivo.close()
