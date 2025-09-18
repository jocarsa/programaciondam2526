Enunciado: Raíz cuadrada segura

Implementa una función raizSegura(numero) que cumpla:

Validación y manejo de errores

Si numero es un valor numérico (int o float) y es mayor o igual a 0 → devuelve su raíz cuadrada.

Si numero es una cadena, intenta convertirla a float y aplica la regla anterior.

Si la conversión falla, o si el número es negativo, la función debe devolver 0.

Usa try/except para capturar errores en la conversión o en el cálculo.

Aserciones

Usa al menos dos assert internos, por ejemplo:

que la salida siempre sea un número (int o float),

que si la entrada es negativa, la salida sea exactamente 0.

Documentación

Escribe un docstring que explique entradas, salidas y qué errores controla.

Estructura del proyecto

Guarda la función en funcionraiz.py.

Crea un archivo main.py que importe la función y realice 3 pruebas de ejemplo mostrando los resultados por pantalla.

Prueba unitaria pequeña

Crea un archivo test_raiz.py que contenga varios assert para verificar:

Caso correcto con número positivo.

Caso con cadena convertible.

Caso con número negativo.

Caso con cadena no convertible.

Caso con 0.
