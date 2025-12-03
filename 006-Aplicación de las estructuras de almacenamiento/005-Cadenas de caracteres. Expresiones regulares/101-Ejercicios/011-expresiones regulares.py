
"""
Explicación del patrón:

^
    Indica el inicio de la cadena. La validación comienza desde el principio.

[a-zA-Z0-9_.+-]+
    Parte local del correo (antes de '@').
    Permite:
        - letras mayúsculas y minúsculas (a-zA-Z)
        - números (0-9)
        - guion bajo (_)
        - punto (.)
        - signo más (+)
        - guion (-)
    El símbolo '+' indica uno o más caracteres válidos.

@
    Caracter obligatorio que separa el usuario del dominio.

[a-zA-Z0-9-]+
    Nombre del dominio principal sin subdominios.
    Permite letras, números y guiones.
    Requiere al menos un carácter.

\.
    Un punto literal que separa el dominio del TLD.
    El backslash escapa el carácter '.' para que no actúe como comodín.

[a-zA-Z0-9-.]+
    Parte final del dominio (TLD o subdominios), por ejemplo:
        .com
        .co.uk
        .org
    Permite letras, números, guiones y puntos.
    El símbolo '+' indica uno o más caracteres.

$
    Indica el final de la cadena. La validación termina aquí.
"""
import re

patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

email_mal = "algo"
email_bien = "info@jocarsa.com"

print(re.match(patron, email_mal))

print(re.match(patron, email_bien))

