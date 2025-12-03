import re

patron = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+[A-Za-z]? \d{5}$'
"""
Explicación del patrón:

^
    Inicio de la cadena.

[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+
    Nombre de la calle o vía.
    Permite:
        - letras mayúsculas y minúsculas
        - letras acentuadas y 'ñ'
        - espacios
    '+' indica uno o más caracteres.

␣ (espacio)
    Separador obligatorio.

\d+
    Número de portal.
    '\d' representa un dígito.
    '+' indica uno o más dígitos.
    Ejemplo: 5, 23, 104

[A-Za-z]?
    Letra opcional en el número (como 10B o 23A).
    '?' indica que puede aparecer cero o una vez.

␣ (espacio)
    Separador obligatorio.

\d{5}
    Código postal español estándar de 5 dígitos.

$
    Final de la cadena.
"""

direccion_mal = "Calle Mayor"
direccion_bien = "Calle Mayor 10 46001"

print(re.match(patron, direccion_mal))
print(re.match(patron, direccion_bien))
