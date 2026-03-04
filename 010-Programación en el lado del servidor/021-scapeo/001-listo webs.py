archivo = open("datos.csv",'r')

lineas = archivo.readlines()

for linea in lineas:
  print(linea)