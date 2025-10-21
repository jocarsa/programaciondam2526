archivo = open("mapa.txt",'r') # READ

lineas = archivo.readlines()

for linea in lineas:
  if "json" in linea:
    print("###########################")
    print("Encontrado!: ",linea)   
     
