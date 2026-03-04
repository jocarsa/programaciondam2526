import requests
from lxml import html

# Abrir archivo con URLs
with open("datos.csv", "r") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    url = linea.strip()  # quitar salto de línea
    try:
        respuesta = requests.get(url, timeout=10)
        arbol = html.fromstring(respuesta.content)
        titulo = arbol.xpath('//title/text()')
        if titulo:
            print(f"{url} -> {titulo[0]}")
        else:
            print(f"{url} -> Sin título encontrado")
    except Exception as e:
        print(f"{url} -> Error: {e}")