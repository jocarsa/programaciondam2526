<?php
	session_start(); // Esto para recordar cosas
  // Si no existe la variable de sesion idioma
  if(!isset($_SESSION['idioma'])){
  	// En ese caso el idioma por defecto es español
  	$_SESSION['idioma'] = 'es';
  }
  // Si la url transporta la variable idioma
  if(isset($_GET['idioma'])){
  	// La sesion es lo que diga la URL
  	$_SESSION['idioma'] = $_GET['idioma'];
  }
	$idioma['es']['inicio'] = "Inicio";
  $idioma['es']['sobremi'] = "Sobre mi";
  $idioma['es']['proyectos'] = "Proyectos";
  $idioma['es']['contacto'] = "Contacto";
  
  $idioma['en']['inicio'] = "Home";
  $idioma['en']['sobremi'] = "About me";
  $idioma['en']['proyectos'] = "Projects";
  $idioma['en']['contacto'] = "Contact";
?>
<!doctype html>
<html lang="es">
  <head>
    <title>Multi idioma</title>
    <meta charset="utf-8">
  </head>
  <body>
    <select>
      <option value="es">🇪🇸</option>
      <option value="en">🇬🇧</option>
    </select>
    <h1>Jose Vicente Carratala</h1>
    <nav>
      <a href=""><?= $idioma[$_SESSION['idioma']]['inicio'] ?></a>
      <a href=""><?= $idioma[$_SESSION['idioma']]['sobremi'] ?></a>
      <a href=""><?= $idioma[$_SESSION['idioma']]['proyectos'] ?></a>
      <a href=""><?= $idioma[$_SESSION['idioma']]['contacto'] ?></a>
    </nav>
  </body>
  <script>
  	
  </script>
</html>