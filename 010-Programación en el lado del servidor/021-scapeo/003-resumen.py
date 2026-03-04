import requests
from lxml import html
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-r1:1.5b"

def describir_web(texto):
    prompt = f"""
Resume en un solo párrafo en español de qué trata la siguiente página web:

{texto[:4000]}
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    respuesta = requests.post(OLLAMA_URL, json=payload, timeout=120)
    return respuesta.json()["response"].strip()


# Abrir archivo con URLs
with open("datos.csv", "r") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    url = linea.strip()

    try:
        print(f"\nProcesando: {url}")

        respuesta = requests.get(url, timeout=10, headers={
            "User-Agent": "Mozilla/5.0"
        })

        arbol = html.fromstring(respuesta.content)

        # Extraer texto visible básico
        parrafos = arbol.xpath('//p//text()')
        texto = " ".join(parrafos)

        if not texto.strip():
            print("No se pudo extraer contenido textual.")
            continue

        descripcion = describir_web(texto)

        print(f"Descripción:\n{descripcion}\n")

    except Exception as e:
        print(f"{url} -> Error: {e}")