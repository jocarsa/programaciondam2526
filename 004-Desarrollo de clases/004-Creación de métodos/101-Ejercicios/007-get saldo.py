class CuentaBancaria():
  def __init__(self):
    self.__saldo = 0
    self.__cliente = ""
    
  # Defino setters y getters para el saldo
  def setSaldo(self,nuevosaldo):
    self.__saldo = nuevosaldo
  def getSaldo(self):
    return self.__saldo
    
cuentecliente1 = CuentaBancaria()
cuentecliente1.setSaldo(10000000000)
print(cuentecliente1.getSaldo())


    
