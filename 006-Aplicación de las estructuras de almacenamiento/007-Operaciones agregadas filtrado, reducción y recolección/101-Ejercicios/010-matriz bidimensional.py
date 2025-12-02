import random

patron = {1,2,3,4,5,6,7,8,9}
sudoku = []
for celda in range(1,10):
  while True:
    lista = []
    for i in range(1,10):
      lista.append(random.randint(1,9))
    conjunto = set(lista)
    if conjunto == patron:
      sudoku.append(lista)
      break # Fuerzo la finalizazión del bucle infinito
    
print(sudoku)
  