<!doctype html>
<html lang="es">
	<head>
  	<title>Camaron viviendas</title>
    <meta charset="utf-8">
    <style>
      *{box-sizing:border-box;margin:0;padding:0;font-family:Arial,Helvetica,sans-serif}
      body{background:#f5f6f7;color:#333;line-height:1.4}
      header,footer{background:#1f2933;color:#fff;text-align:center;padding:1rem}
      nav{background:#fff;padding:1rem;border-bottom:1px solid #ddd}
      nav form{max-width:600px;margin:auto;display:flex;gap:.5rem}
      select,input[type=submit]{padding:.5rem;font-size:1rem}
      select{flex:1}
      input[type=submit]{background:#2563eb;color:#fff;border:none;cursor:pointer}
      input[type=submit]:hover{background:#1d4ed8}
      main{max-width:1200px;margin:2rem auto;padding:0 1rem}
      section{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem}
      article{background:#fff;border:1px solid #ddd;border-radius:4px;padding:1rem}
      article h3{margin-bottom:.5rem;color:#2563eb}
      article p{font-size:.9rem;margin:.2rem 0}
      footer{font-size:.85rem;margin-top:2rem}
    </style>

  </head>
  <body>
  	<header><h1>Camarón viviendas</h1></header>
    <nav>
    	<form action="?" method="POST">
      	<select name="localidad">
        	<option>Selecciona una localidad...</option>
          <option value="Valencia">Valencia</option>
          <option value="Alboraya">Alboraya</option>
          <option value="Torrent">Torrent</option>
          <option value="Gandía">Gandía</option>
          <option value="Sagunto">Sagunto</option>
          <option value="Paterna">Paterna</option>
          <option value="Burjassot">Burjassot</option>
          <option value="Xàtiva">Xàtiva</option>
          <option value="Cullera">Cullera</option>
        </select>
        <input type="submit">
      </form>
    </nav>
    <main>
    	<section>
      	<?php
          $host = "localhost";
          $user = "camaron";
          $pass = "Camaron123$";
          $db   = "camaron";

          $conexion = new mysqli($host, $user, $pass, $db);
          $resultado = $conexion->query("
            SELECT * FROM viviendas WHERE localidad = '".$_POST['localidad']."';
          ");
          while ($fila = $resultado->fetch_assoc()) {
            echo '
            	<article>
              	<h3>'.$fila['localidad'].'</h3>
                <p>'.$fila['precio'].'</p>
                <p>'.$fila['metroscuadrados'].'</p>
                <p>'.$fila['aniodeconstruccion'].'</p>
                <p>'.$fila['direccion'].'</p>
                <p>'.$fila['altura'].'</p>
                <p>'.$fila['tipodevivienda'].'</p>
                <p>'.$fila['descripcion'].'</p>
                <p>'.$fila['estado'].'</p>
                <p>'.$fila['banios'].'</p>
                <p>'.$fila['habitaciones'].'</p>
                <p>'.$fila['teniente'].'</p>
              </article>
            ';
          }
    		?>
      </section>
    </main>
    <footer>(c) 2026 No me puedo creer que este proyecto se llame Camarón</footer>
  </body>
</html>