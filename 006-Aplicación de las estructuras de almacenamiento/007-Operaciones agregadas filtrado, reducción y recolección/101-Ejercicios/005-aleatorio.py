import random

patron = {1,2,3,4,5,6,7,8,9}

lista = []
for i in range(1,10):
	lista.append(random.randint(1,9))
print(patron)
print(lista)
conjunto = set(lista)
print(conjunto)

if conjunto == patron:
  print("El conjunto es correcto")
else:
  print("El conjunto no es correcto")