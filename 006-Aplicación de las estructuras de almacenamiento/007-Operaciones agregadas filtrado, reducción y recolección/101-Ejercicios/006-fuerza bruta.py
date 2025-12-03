import random

patron = {1,2,3,4,5,6,7,8,9}

while True:
  lista = []
  for i in range(1,10):
    lista.append(random.randint(1,9))
    
  conjunto = set(lista)
  print(lista)
  
  if conjunto == patron:
    print("El conjunto es correcto")
    print(conjunto)
    print(lista)
    break # Fuerzo la finalizazión del bucle infinito
    

  