import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5-coder:7b"

# Read HTML file
with open("guardado.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Build prompt using file contents
prompt = f"""
Este HTML es el volcado de una página web de una inmobiliaria.
Dentro del texto, escondida, hay información acerca de una serie de casas.
Extrae esta información. Genera un listado de las diferentes casas que encuentres.
No comentes el HTML de la página, tampoco lo reestructures.
Solo quiero saber los datos de las casas que se contienen en este archivo.

HTML CONTENT:
{html_content}
"""

data = {
    "model": MODEL,
    "prompt": prompt,
    "stream": False
}

req = urllib.request.Request(
    OLLAMA_URL,
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read().decode("utf-8"))
    print(result["response"])
