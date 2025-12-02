import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    contador = 0
    patron = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    sudoku = []

    for celda in range(1, 10):
        while True:
            contador += 1
            lista = []
            for i in range(1, 10):
                lista.append(random.randint(1, 9))
            conjunto = set(lista)
            if conjunto == patron:
                sudoku.append(lista)
                break  # Fuerzo la finalización del bucle infinito

    print("He necesitado, con fuerza bruta, " + str(contador) + " intentos")
    return render_template("index.html", datos=sudoku)

if __name__ == "__main__":
    app.run(debug=True)
