Descripción

Crea un programa por consola que simule un duelo relámpago entre un mago y un hechizo protector.

Entrada con validación

Pide la edad del mago. Convierte a int con try/except.

Si falla, usa edad 100 por defecto.

Clasificación y poder base (selección + función)

Clasifica al mago según su edad:

<30 → Aprendiz

30–99 → Hechicero

≥100 → Archimago

Implementa poderBase(edad) -> int que devuelva:

Aprendiz → 5

Hechicero → 8

Archimago → 10

(documenta la función con un docstring).

Rompimiento del hechizo (bucle + selección)

El escudo mágico empieza con 15 puntos de energía.

Recorre dos turnos con un for de 1 a 2:

Turno 1 → “Hechizo de Fuego” → daño = poderBase // 2

Turno 2 → “Hechizo de Rayo” → daño = poderBase // 3

Resta el daño al escudo.

Si la energía del escudo baja de 0, ajústala a 0 y sal del bucle.

Aserciones mínimas

Tras calcular cada daño: assert que el daño es numérico y ≥ 0.

Tras ajustar la energía: assert que la energía es ≥ 0.

Salida

Muestra: edad, rango del mago, poder base, energía final del escudo y resultado:

Si la energía es 0 → “¡El mago rompe el escudo mágico!”

Si no → “El escudo resiste al duelo relámpago.”


# pedir edad
edad_mago = input("Introduce la edad del mago: ")
# convertir a entero
try:
  edad_mago = int(edad_mago)
except: 
  # si falla, pon 100
  edad_mago = 100

# clasifica por edad
# menor que 30 es Aprendiz
# de 30 a 99 es Hechicero
# mas de 100 es Archimago

# funcion poderBase, recibe edad, devuelve entero
# si es aprendiz, devuelve 5
# si es hechicero, devuelve 8
# si es archimago, devuelve 10

# empezamos bucle
# escudo empieza con 15 puntos
# recorre dos turnos con for
# turno 1 fuego daño = poderBase // 2
# turno 2 hechizo rayo = daño = poderBase // 3
# resta el daño al escudo
# si energia escudo baja de cero, ajusta a cero

# tras cada daño, print de daño y mayor que cero
# tras ajuste energia, print y energia es mayor que cero

# salida: edad, rango, poder base, energia del escudo
# energia es cero, mago rompe escudo
# energia mayor que cero, escudo resiste duelo

