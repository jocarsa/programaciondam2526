from flask import Flask, render_template, request
import io
import contextlib


app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("frente.html")

@app.route("/api", methods=['POST'])
def api():
    codigo = request.data.decode("utf-8")

    buffer = io.StringIO()
    try:
        # Ejecuta el código y captura todo lo que se imprima
        with contextlib.redirect_stdout(buffer):
            exec(codigo, {})   # entorno global vacío (peligroso igualmente si no controlas el código)
    except Exception as e:
        return str(e), 400

    salida = buffer.getvalue()
    # Si no ha habido nada por pantalla, puedes devolver algo por defecto
    return salida if salida else "OK"

if __name__ == "__main__":
  app.run(debug=True)
