import json

archivo = open("blog.json",'r')

contenido = json.load(archivo)

print(contenido)

