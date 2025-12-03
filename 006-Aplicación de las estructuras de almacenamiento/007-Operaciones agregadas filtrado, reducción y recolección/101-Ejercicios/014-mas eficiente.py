import random
from flask import Flask, render_template

app = Flask(__name__)


def es_valido(grid, fila, col, num):
    """Comprueba si `num` puede ponerse en grid[fila][col]."""

    # Fila
    if num in grid[fila]:
        return False

    # Columna
    for f in range(9):
        if grid[f][col] == num:
            return False

    # Bloque 3x3
    bloque_fila = (fila // 3) * 3
    bloque_col = (col // 3) * 3
    for f in range(bloque_fila, bloque_fila + 3):
        for c in range(bloque_col, bloque_col + 3):
            if grid[f][c] == num:
                return False

    return True


def resolver_sudoku(grid):
    """
    Backtracking: intenta rellenar la cuadrícula.
    Devuelve True si se ha podido resolver, False si no.
    """

    # Buscar la siguiente celda vacía (0)
    for fila in range(9):
        for col in range(9):
            if grid[fila][col] == 0:
                # Probamos números del 1 al 9 en orden aleatorio
                candidatos = list(range(1, 10))
                random.shuffle(candidatos)

                for num in candidatos:
                    if es_valido(grid, fila, col, num):
                        grid[fila][col] = num
                        if resolver_sudoku(grid):
                            return True
                        # backtrack
                        grid[fila][col] = 0

                # Si ningún número sirve, devolvemos False
                return False

    # Si no quedan celdas vacías, está resuelto
    return True


def generar_sudoku_completo():
    """Genera un sudoku completo válido (9x9) usando backtracking."""
    grid = [[0 for _ in range(9)] for _ in range(9)]
    resolver_sudoku(grid)
    return grid


def sudoku_a_bloques(sudoku):
    """
    Convierte el sudoku (9x9) en 9 bloques 3x3.
    Cada bloque es una lista de 9 números.
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
    sudoku = generar_sudoku_completo()
    datos = sudoku_a_bloques(sudoku)
    return render_template("index2.html", datos=datos)


if __name__ == "__main__":
    app.run(debug=True)
