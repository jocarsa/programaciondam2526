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
            exec(codigo, {})
    except Exception as e:
        # devolvemos el error como texto y código 400
        return str(e), 400

    salida = buffer.getvalue()
    return salida if salida else "OK"

if __name__ == "__main__":
    app.run(debug=True)
