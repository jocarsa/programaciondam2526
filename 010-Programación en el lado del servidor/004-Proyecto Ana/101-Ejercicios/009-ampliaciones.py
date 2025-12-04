from flask import Flask, render_template, request
import io
import contextlib
import traceback

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("frenteampliado.html")

@app.route("/api", methods=['POST'])
def api():
    data = request.get_json(force=True)
    codigo = data.get("code", "")
    entradas = data.get("inputs", "")

    # Preparamos las líneas de entrada para input()
    input_lines = iter(entradas.splitlines())

    buffer = io.StringIO()

    def custom_input(prompt=""):
        # Mostrar el prompt en la salida
        print(prompt, end="", file=buffer)
        try:
            linea = next(input_lines)
            # Mostrar lo que "escribe" el usuario en la misma terminal
            print(linea, file=buffer)
            return linea
        except StopIteration:
            # No quedan más líneas de entrada
            print("\n[AVISO] No quedan más líneas de entrada (stdin). Se devuelve cadena vacía.", file=buffer)
            return ""

    # Entorno de ejecución
    global_env = {
        "__name__": "__main__",
        "input": custom_input,
    }

    try:
        with contextlib.redirect_stdout(buffer):
            with contextlib.redirect_stderr(buffer):
                exec(codigo, global_env)
    except Exception:
        error_text = traceback.format_exc()
        return error_text, 400

    salida = buffer.getvalue()
    return salida if salida else "OK"

if __name__ == "__main__":
    app.run(debug=True)
