<?php
	// Esto ha empezado siendo un copia pega de eliminar
  // Y luego lo modifica
  
  // Primero recojo lo que viene del formulario
  
	$titulo = $_POST['titulo'];	
  $contenido = $_POST['contenido'];	
  $fecha_publicacion = $_POST['fecha_publicacion'];	
  $autor_id = $_POST['autor_id'];	
  $id = $_POST['id'];																// Atrapo el id a eliminar
	
  // Ahora me conecto a la base de datos
  
  $host = "localhost";															// Me conecto a la base de datos
  $user = "periodico";
  $pass = "Periodico123$";
  $db   = "periodico";

  $conexion = new mysqli($host, $user, $pass, $db);	// Ejecuto la conexion

	// Le lanzo una peticion de actualización

  $sql = "
    UPDATE noticias
    SET 
    titulo = '".$titulo."',
    contenido = '".$contenido."',
    fecha_publicacion = '".$fecha_publicacion."',
    autor_id = ".$autor_id."
    WHERE id = ".$id.";
  ";	// Preparo la peticion																							// Lanzo la peticion de insert
  echo $sql;
  $conexion->query($sql);														// Ejecuto la peticion
	
  // Y cierro y vuelvo
  
  $conexion->close();																// Cierro la conexion
  header("Location: ../../escritorio.php");					// Y me vuelvo al escritorio
  
?>