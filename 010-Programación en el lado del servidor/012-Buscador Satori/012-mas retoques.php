<!doctype html>
<html lang="es">
  <head>
    <title>Satori</title>
    <meta charset="utf-8">
    <style>
    	body,html{padding:0px;margin:0px;font-family:sans-serif;}
      header{display:flex;justify-content:center;align-items:center;gap:20px;
      padding:20px;}
      main{margin:auto;width:800px;}
      article{border-bottom:1px solid lightgray;margin:20px;padding:20px;}
      h1,h2,h3{padding:0px;margin:0px;}
      a{font-size:10px;}
      input{border:1px solid lightgrey;padding:10px;border-radius:20px;}
      header img{width:50px;}
    </style>
  </head>
  <body>
    <header>
    	<img src="satorilogo.png">
      <h1>Satori</h1>
      <form method="POST" action="?">
        <input 
        	type="text" 
          name="criterio" 
          placeholder="Introduce algo para buscar..."
          value="<?= $_POST['criterio'] ?>">
      </form>
    </header>
    <main>
    	<?php
      	
        $host = "localhost";
        $user = "satori";
        $pass = "Satori123$";
        $db   = "satori";

        $conexion = new mysqli($host, $user, $pass, $db);
        
        $resultado = $conexion->query("
          SELECT * FROM paginas WHERE titulo LIKE '%".$_POST['criterio']."%';
        ");	// Comparador LIKE '%xxxxxx%'
        while ($fila = $resultado->fetch_assoc()) { ?>
      	<article>
          <h3><?= $fila['titulo'] ?></h3>
          <a href="<?= $fila['url'] ?>"><?= $fila['url'] ?></a>
        </article>
      <?php } ?>
    </main>
  </body>
</html>