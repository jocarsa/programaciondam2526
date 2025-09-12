''' 
    Calculadora de cuadras
    v0.1 (c) 2025 Jose Vicente Carratalá
    Programa que calcula número de cuadras a partir de los caballos
'''

import math as matematicas

# Datos de inicio
caballos = 0
cuadras = 0
caballos_por_cuadra = 0

# Entrada de información
caballos_por_cuadra = int(input("Introduce el número de caballos por cuadra: "))
caballos = int(input("Introduce el número de caballos: "))

# Realización de cálculos
cuadras = caballos / caballos_por_cuadra
redondeoalza = matematicas.ceil(cuadras)

# Salida de resultados
print("Si tienes",caballos,"caballos")
print("Y te caben tres caballos por cuadra")
print("En ese caso necesitas",redondeoalza,"cuadras")


