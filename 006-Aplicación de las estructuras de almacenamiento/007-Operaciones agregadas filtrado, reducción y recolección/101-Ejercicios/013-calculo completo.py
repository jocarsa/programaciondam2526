import random
from flask import Flask, render_template

app = Flask(__name__)

PATRON = set(range(1, 10))  # {1,2,3,4,5,6,7,8,9}


def generar_fila():
    """Genera una permutación aleatoria de 1..9."""
    fila = list(range(1, 10))
    random.shuffle(fila)
    return fila


def filas_validas(sudoku):
    """Todas las filas contienen exactamente los números 1..9."""
    for fila in sudoku:
        if set(fila) != PATRON:
            return False
    return True


def columnas_validas(sudoku):
    """Todas las columnas contienen exactamente los números 1..9."""
    for c in range(9):
        columna = [sudoku[f][c] for f in range(9)]
        if set(columna) != PATRON:
            return False
    return True


def sudoku_a_bloques(sudoku):
    """
    Convierte el sudoku (9 filas x 9 columnas) en 9 bloques 3x3.
    Cada bloque es una lista de 9 números, en orden de lectura.
    """
    bloques = []
    for br in range(3):          # bloque fila
        for bc in range(3):      # bloque columna
            bloque = []
            for r in range(br * 3, br * 3 + 3):
                for c in range(bc * 3, bc * 3 + 3):
                    bloque.append(sudoku[r][c])
            bloques.append(bloque)
    return bloques


@app.route("/")
def inicio():
    intentos = 0

    # Fuerza bruta: generar tableros al azar hasta que filas y columnas sean válidas
    while True:
        intentos += 1
        sudoku = [generar_fila() for _ in range(9)]

        if filas_validas(sudoku) and columnas_validas(sudoku):
            break

    print(f"He necesitado, con fuerza bruta, {intentos} intentos")

    # Adaptamos a tu HTML: 9 bloques 3x3
    datos = sudoku_a_bloques(sudoku)

    return render_template("index.html", datos=datos)


if __name__ == "__main__":
    app.run(debug=True)
