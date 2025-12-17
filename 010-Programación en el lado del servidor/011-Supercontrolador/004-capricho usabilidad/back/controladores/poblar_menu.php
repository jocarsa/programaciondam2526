<?php
	// Ahora lo que quiero es un listado de las tablas en la base de datos
	$resultado = $conexion->query("
   SHOW TABLES;
  ");
  while ($fila = $resultado->fetch_assoc()) {
  	$clase = "";							// De entrada no tienes clase	
    if($fila['Tables_in_'.$db] == $_GET['tabla']){	// Pero si el nombre de esta tabla coincide con la tabla cargada
    	$clase  = "activo";			// En ese caso tu clase es "activo"
    }
     echo '
     	<a href="?tabla='.$fila['Tables_in_'.$db].'" class="'.$clase.'">
      	'.$fila['Tables_in_'.$db].'
      </a>
      ';
  }
?>
<style>
	.activo{
  	transform:translateX(20px);
  }
</style>