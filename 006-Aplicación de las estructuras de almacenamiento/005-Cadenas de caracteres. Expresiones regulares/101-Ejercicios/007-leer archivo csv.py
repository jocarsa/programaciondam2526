archivo = open("clientes.csv","r")

lineas = archivo.readlines()

for linea in lineas:
	partido = linea.split(",")
	print(partido)