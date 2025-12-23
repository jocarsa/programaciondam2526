<form action="inc/create/procesaformulario.php" method="POST">
	<div class="controlformulario">
    <label for="titulo">Título de la nueva noticia</label>
    <input type="text" name="titulo" id="titulo">
  </div>
  
  <div class="controlformulario">
  	<label for="contenido">Contenido de la nueva noticia</label>
		<textarea id="contenido" name="contenido"></textarea>
  </div>
  
  <div class="controlformulario">
  	<label for="fecha_publicacion">Fecha de la nueva noticia</label>
		<input type="text" name="fecha_publicacion" id="fecha_publicacion">
  </div>
  
  <div class="controlformulario">
  	<label for="autor_id">Autor de la nueva noticia</label>
		<input type="text" name="autor_id" id="autor_id">
  </div>
  
  <input type="submit">
  
</form>