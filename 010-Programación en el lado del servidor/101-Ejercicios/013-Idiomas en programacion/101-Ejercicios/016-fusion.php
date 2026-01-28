<?php
// PREPARAMOS LA SESION ///////////////////////////////////////
session_start();

if (!isset($_SESSION['idioma'])) {
  $_SESSION['idioma'] = 'es';
}
if (isset($_GET['idioma'])) {
  $_SESSION['idioma'] = $_GET['idioma'];
}

// CARGAMOS IDIOMAS DEL CSV /////////////////////////////
$idioma = [];

$rows = array_map('str_getcsv', file(__DIR__ . '/idiomas.csv'));
$header = array_shift($rows); // ['clave','es','en',...]

foreach ($rows as $row) {
  if (!$row) continue;
  // Normaliza longitud (por si alguna fila viene más corta)
  $row = array_pad($row, count($header), '');

  $data = array_combine($header, $row);
  if (!isset($data['clave'])) continue;

  $clave = trim($data['clave']);
  if ($clave === '') continue;

  foreach ($data as $lang => $value) {
    if ($lang === 'clave') continue;
    $idioma[$lang][$clave] = $value; // <-- aquí se rellena de verdad
  }
}

// Si el idioma pedido no existe en el CSV, vuelve a 'es'
if (!isset($idioma[$_SESSION['idioma']])) {
  $_SESSION['idioma'] = 'es';
}
?>
<!doctype html>
<html lang="es">
  <head>
    <title>Multi idioma</title>
    <meta charset="utf-8">
    <style>
      body,html{padding:0px;margin:0px;font-family:sans-serif;}
      header{display:flex;background:black;color:white;justify-content:space-between;align-items:center;}
      header a{text-decoration:none;color:inherit;margin:0px 10px;}
      h1{font-size:20px;}
      select{background:none;border:none;color:white;}
      option{color:black;}
    </style>
  </head>
  <body>
    <header>
      <h1>Jose Vicente Carratala</h1>
      <nav>
        <a href=""><?= htmlspecialchars($idioma[$_SESSION['idioma']]['inicio'] ?? 'Inicio') ?></a>
        <a href=""><?= htmlspecialchars($idioma[$_SESSION['idioma']]['sobremi'] ?? 'Sobre mí') ?></a>
        <a href=""><?= htmlspecialchars($idioma[$_SESSION['idioma']]['proyectos'] ?? 'Proyectos') ?></a>
        <a href=""><?= htmlspecialchars($idioma[$_SESSION['idioma']]['contacto'] ?? 'Contacto') ?></a>
      </nav>

      <select id="idioma">
        <option value="es" <?= ($_SESSION['idioma'] === 'es') ? 'selected' : '' ?>>🇪🇸</option>
        <option value="en" <?= ($_SESSION['idioma'] === 'en') ? 'selected' : '' ?>>🇬🇧</option>
      </select>
    </header>

    <script>
      const selector = document.querySelector("#idioma");
      selector.addEventListener("change", function () {
        window.location = "?idioma=" + encodeURIComponent(this.value);
      });
    </script>
  </body>
</html>
