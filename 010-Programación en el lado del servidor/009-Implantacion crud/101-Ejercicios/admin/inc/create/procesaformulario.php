<?php

  $titulo = $_POST['titulo'];												// Atrapo el titulo que viene del formulario
  $contenido = $_POST['contenido'];									// Atrapo el contenido que viene del formulario
  $fecha_publicacion = $_POST['fecha_publicacion'];	// Atrapo la fecha de publiacion que viene del formulario
  $autor_id = $_POST['autor_id'];										// Atrapo el id de autor

  $host = "localhost";															// Me conecto a la base de datos
  $user = "periodico";
  $pass = "Periodico123$";
  $db   = "periodico";

  $conexion = new mysqli($host, $user, $pass, $db);	// Ejecuto la conexion

  $sql = "
  	INSERT INTO noticias VALUES(
    	NULL,
      '".$titulo."',
      '".$contenido."',
      '".$fecha_publicacion."',
     	".$autor_id."
    );
  ";																								// Lanzo la peticion de insert
  $conexion->query($sql);
	
  $conexion->close();																// Cierro la conexion
  header("Location: ../../escritorio.php");												// Y me vuelvo al escritorio
  
?>