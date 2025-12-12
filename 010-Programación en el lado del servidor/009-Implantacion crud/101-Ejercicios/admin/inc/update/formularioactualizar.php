<?php

// Primero traemos el formulario de insertar
// Y luego lo rellenamos de datos (los datos a actualizar)

		$host = "localhost";
    $user = "periodico";
    $pass = "Periodico123$";
    $db   = "periodico";

    $conexion = new mysqli($host, $user, $pass, $db);

    $sql = "SELECT * FROM noticias WHERE id = ".$_GET['id'].";";

    $resultado = $conexion->query($sql);
    while ($fila = $resultado->fetch_assoc()) {
?>

    <form action="inc/update/procesaformulario.php" method="POST">
    	<!-- CORREGID ESTA LINEA -->
    	<input type="hidden" name="id" value="<?= $fila['id'] ?>"> <!-- OJO A ESTE CAMPO OCULTO -->
      <!-- CORREGID ESTA LINEA -->
      <div class="controlformulario">
        <label for="titulo">Título de la nueva noticia</label>
        <input type="text" name="titulo" id="titulo" value="<?= $fila['titulo'] ?>">
      </div>

      <div class="controlformulario">
        <label for="contenido">Contenido de la nueva noticia</label>
        <textarea id="contenido" name="contenido"><?= $fila['contenido'] ?></textarea>
      </div>

      <div class="controlformulario">
        <label for="fecha_publicacion">Fecha de la nueva noticia</label>
        <input type="text" name="fecha_publicacion" id="fecha_publicacion" value="<?= $fila['fecha_publicacion'] ?>">
      </div>

      <div class="controlformulario">
        <label for="autor_id">Autor de la nueva noticia</label>
        <input type="text" name="autor_id" id="autor_id" value="<?= $fila['autor_id'] ?>">
      </div>

      <input type="submit">

    </form>

<?php

	} 

?>