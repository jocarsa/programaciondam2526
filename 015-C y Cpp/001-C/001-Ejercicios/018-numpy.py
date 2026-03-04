import numpy as np
import time

inicio = time.perf_counter()

numero = 1.0000000432
N = 235324544

numero = numero * np.power(1.00000000645, N)

fin = time.perf_counter()

tiempo = fin - inicio

print("El resultado es:", numero)
print("Tiempo de ejecucion:", tiempo, "segundos")