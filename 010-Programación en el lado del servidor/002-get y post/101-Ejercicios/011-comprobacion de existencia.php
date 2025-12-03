<?php
	// Comprobación de existencia isset
	if(isset($_POST['nombre'])){
		echo $_POST['nombre'];
  }
?>

<form action="?" method="POST">
  <p>Introduce tu nombre</p>
  <input type="text" name="nombre">
  <input type="submit">
</form>
