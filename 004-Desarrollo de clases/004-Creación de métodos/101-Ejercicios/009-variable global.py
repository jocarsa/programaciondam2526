limitediferenciasaldo = 1000

class CuentaBancaria():
  def __init__(self):
    self.__saldo = 0
    self.__cliente = ""
    
  # Defino setters y getters para el saldo
  def setSaldo(self,nuevosaldo):
    # Establezco una condicion de que valida si el saldo nuevo es mayor de 1000 euros
    if nuevosaldo > self.__saldo + limitediferenciasaldo:
      # Si salta la alarma, avisa y NO cambia el saldo
      print("Voy a avisar a la entidad de un ingreso muy grande")
    else
      # Si pasa el filtro, solo entonces se cambia el saldo
      self.__saldo = nuevosaldo
      
  def getSaldo(self):
    return self.__saldo
    
cuentacliente1 = CuentaBancaria()
cuentacliente1.setSaldo(10000000000)
print(cuentacliente1.getSaldo())


    
