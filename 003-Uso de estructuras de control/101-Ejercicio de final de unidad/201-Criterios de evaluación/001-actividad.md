

# Actividad (30’): “Adivina el número — Modo docente”

Crea un script `adivina.py` que juegue a adivinar un número secreto entre 1 y 50 con un máximo de **6 intentos**. Debe usar condicionales `if/elif/else`, bucles `while`, saltos (`break/continue`), manejo de errores con `try/except` y al menos **2 aserciones** para garantizar invariantes. 

## Objetivos de aprendizaje

* Aplicar **selección** con `if/elif/else` para comparar el intento con el secreto. 
* Usar **repetición** con `while` y contador de intentos. 
* Practicar **saltos** con `break` (acierto) y `continue` (entrada inválida). 
* Validar entradas con **`try/except`** y documentar brevemente con docstrings. 
* Añadir **aserciones** para límites y estado. 

## Requisitos funcionales

1. El programa elige al inicio un **número secreto** en `[1,50]`.
2. El usuario tiene **6 intentos**. En cada intento:

   * Pide un número por `input`. Si no es convertible a `int`, **muestra aviso** y **no gasta intento** (usa `continue`). 
   * Si está **fuera de rango** (`<1` o `>50`), avisa y **no gasta intento**.
   * Compara con `if/elif/else`: imprime “**Demasiado alto**” o “**Demasiado bajo**”; si acierta, **termina con `break`**. 
3. **Pista de paridad**: al **3er** intento consumido (y si no ha acertado), muestra si el secreto es **par o impar**. (Selección + contador). 
4. Al final, muestra **resultado** (ganó/perdió) y el número secreto.
5. **Aserciones mínimas**:

   * El número secreto **siempre** está en `[1,50]`.
   * El contador de intentos **nunca** es negativo. 


