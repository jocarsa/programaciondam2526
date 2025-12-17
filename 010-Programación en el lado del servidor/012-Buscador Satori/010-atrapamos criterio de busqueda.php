<!doctype html>
<html lang="es">
  <head>
    <title>Satori</title>
    <meta charset="utf-8">
    <style>
    	body,html{padding:0px;margin:0px;font-family:sans-serif;}
      header{display:flex;justify-content:center;align-items:center;gap:20px;}
      main{margin:auto;width:800px;}
      article{border-bottom:1px solid lightgray;margin:20px;padding:20px;}
      h1,h2,h3{padding:0px;margin:0px;}
    </style>
  </head>
  <body>
    <header>
      <h1>Satori</h1>
      <form method="POST" action="?">
        <input type="text" name="criterio">
      </form>
    </header>
    <main>
    	<?php
      	if(isset($_POST['criterio'])){
        	echo "Lo que vas a buscar es: ".$_POST['criterio'];
        }
      ?>
    	<?php for($i = 0;$i<30;$i++){ ?>
        <article>
          <h2>Titulo de la web</h2>
          <a href="https://ejemplo.com">https://ejemplo.com</a>
        </article>
      <?php } ?>
    </main>
  </body>
</html>