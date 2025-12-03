# Abre una terminal e instala flask:
# pip install flask
# Flask es un microservidorweb que nos permite generar HTML desde Python

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  return "Esto es HTML desde Flask"
  
# Ahora arranco el servidor
if __name__ == "__main__":
  aplicacion.run(debug=True)
