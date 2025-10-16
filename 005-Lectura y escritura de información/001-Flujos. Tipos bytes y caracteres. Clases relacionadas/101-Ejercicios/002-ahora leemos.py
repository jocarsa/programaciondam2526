archivo = open("clientes.txt",'r') # R = Read

contenido = archivo.readline()
# También existe archivo.readlines()

print(contenido)

archivo.close()



