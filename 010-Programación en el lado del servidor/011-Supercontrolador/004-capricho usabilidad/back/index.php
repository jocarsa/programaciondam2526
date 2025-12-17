<!doctype html>
<html>
	<head>
  	<link rel="stylesheet" href="css/estilo.css">
  </head>
  <body>
		<?php include "inc/conexion_bd.php"; ?>
    <nav>
    	<?php include "controladores/poblar_menu.php" ?>
    </nav>
    <main>
      <?php
      	// Enrutador: se encarga de manejar las operaciones a mostrar
      	if(!isset($_GET['operacion'])){ // Si no hay operacion
      		include "controladores/leer.php";
        }else{
        	if($_GET['operacion'] == "insertar"){
          	include "controladores/insertar.php";
          }
        }
      ?>
    </main>
  </body>
</html>