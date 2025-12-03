Terminal:

sudo chmod 777 -R /var/www/html/programaciondam2526

sudo = Realizo acción como administrador

chmod = cambio permisos

777 = le doy permiso a todo el mundo

-R = Lo quiero aplicar recursivo (a todo el contenido)

/var/www.... = la carpeta afectada

En el sistema de permisos UNIX (Linux,macOS)

1 numero para el usuario
1 numero para el grupo al que pertenece el usuario
1 numero para todo el resto


0 - ningún permiso
1 = solo ejectar
2 = solo escribir
3 = escribir y ejecutar
4 = solo leer
5 = leer y ejecutar
6 = leer y escribir
7 = leer, escribir y ejecutar

777 = permisible en tu maquina, no recomendable en produccion
usuario leer, escribir y ejecutar
grupo leer, escribir y ejecutar
todo el mundo leer, escribir y ejecutar

755 = posible para produccion
usuario leer, escribir y ejecutar
grupo leer y ejecutar
todo el mundo leer y ejecutar

644 = mas restrictivo para produccion
usuario leer y escribir
grupo solo leer
todo el mundo solo leer





