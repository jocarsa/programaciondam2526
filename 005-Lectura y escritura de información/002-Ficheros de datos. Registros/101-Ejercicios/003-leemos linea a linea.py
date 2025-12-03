import json

archivo = open("blog.json",'r')

contenido = json.load(archivo)

for linea in contenido:
  print(linea)

