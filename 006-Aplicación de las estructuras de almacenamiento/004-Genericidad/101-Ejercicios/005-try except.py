numeros = [1,2,"3",4,"cinco"]

print(numeros)

def calculaDoble():
  for numero in numeros:
    try:
      numero = int(numero)   # Convierto en entero
      print(numero*2)
    except:
      print("(no válido)")

calculaDoble()
