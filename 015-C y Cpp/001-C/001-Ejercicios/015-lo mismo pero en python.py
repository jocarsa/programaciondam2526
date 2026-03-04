import time

inicio = time.perf_counter()

numero = 1.0000000432

for contador in range(235324544):
    numero = numero * 1.00000000645

fin = time.perf_counter()

tiempo = fin - inicio

print("El resultado es:", numero)
print("Tiempo de ejecucion:", tiempo, "segundos")