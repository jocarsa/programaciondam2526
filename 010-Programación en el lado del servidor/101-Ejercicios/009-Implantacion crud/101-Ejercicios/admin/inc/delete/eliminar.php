<?php

  $id = $_GET['id'];																// Atrapo el id a eliminar

  $host = "localhost";															// Me conecto a la base de datos
  $user = "periodico";
  $pass = "Periodico123$";
  $db   = "periodico";

  $conexion = new mysqli($host, $user, $pass, $db);	// Ejecuto la conexion

  $sql = "DELETE FROM noticias WHERE id = ".$id.";";	// Preparo la peticion																							// Lanzo la peticion de insert
  $conexion->query($sql);														// Ejecuto la peticion
	
  $conexion->close();																// Cierro la conexion
  header("Location: escritorio.php");					// Y me vuelvo al escritorio
  
?>