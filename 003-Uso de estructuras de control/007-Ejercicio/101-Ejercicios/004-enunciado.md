Descripción

Registro de dragones (entrada del usuario)

Pide por consola nombre y edad de cada dragón: Dragón A y Dragón B.

Convierte la edad a entero con try/except. Si falla, usa un valor por defecto (p. ej., 100 años).

Clasifica cada dragón por edad con condicionales:

< 50 → “Joven”

50–199 → “Adulto”

≥ 200 → “Anciano”

Entrenamiento (bucle for)

Simula 3 días de entrenamiento por dragón con un for.

Cada día incrementa:

fuerza (p. ej., +2 por día si es Joven, +1 si es Adulto, +1 si es Anciano).

resistencia (regla similar).

Muestra por pantalla el progreso de cada día (una línea por día).

Funciones obligatorias

calculaFuerzaBase(edad) -> int
Devuelve una fuerza inicial según la categoría (elige una regla y documéntala).

turnoDeAtaque(fuerza, resistenciaEnemigo) -> int
Calcula el daño de un ataque y lo devuelve (no hagas print dentro).

Duelo (bucle while)

Inicializa salud de cada dragón (p. ej., 30–50 puntos, a tu elección).

En un while que termine cuando uno llegue a salud ≤ 0:

Turno alterno: A golpea a B y luego B a A (usa un contador de turnos).

En cada golpe, llama a turnoDeAtaque(...) y resta salud al rival.

Si la salud cae por debajo de 0, ajústala a 0 y termina el bucle.

Puedes usar un for interno para contar “subturnos” o “intentos” del ataque (por ejemplo, 2 mordiscos por turno).

Manejo de errores

Cualquier entrada (edad, confirmaciones) debe pasar por try/except.

Aserciones

Incluye al menos 2 assert:

Que la salud nunca sea negativa tras un ajuste.

Que el daño devuelto por turnoDeAtaque sea numérico y ≥ 0.

Salida final

Muestra un resumen: nombres, categorías, fuerza final, resistencia final, y ganador del duelo.
