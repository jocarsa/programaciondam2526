numeros = [1,2,"3",4]

print(numeros)

def calculaDoble():
  for numero in numeros:
    numero = int(numero)   # Convierto en entero
    print(numero*2)

calculaDoble()
