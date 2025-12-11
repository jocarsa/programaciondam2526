<!--http://..../basesdedatosdamdaw2526/008-Proyectos/003-Panel%20de%20control/101-Ejercicios/aplicacion/admin/escritorio.php -->

<!doctype html>
<html lang="es">
	<head>
  	<title>El jocarsa - Panel de control</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/estilo.css">
  </head>
  <body>
  	<nav>
    	<button>Noticias</button>
      <button>Autores</button>
    </nav>
    <main>
    	<table>
      	<thead>
        	<tr>
          	<th>Titulo</th><th>Texto</th><th>Fecha</th><th>Autor</th><th>Categoria</th>
          </tr>
        </thead>
        <tbody>
        	<?php
          	for($i = 0;$i<20;$i++){
            	echo '
                <tr>
                  <td>Titulo</td><td>Texto</td><td>Fecha</td><td>Autor</td><td>Categoria</td>
                </tr>
              	';
            }
          ?>
        </tbody>
      </table>
    </main>
  </body>
</html>