<?php include "inc/cabecera.php"; ?>

  <?php
    $host = "localhost";
    $user = "tiendaonlinedamdaw";
    $pass = "Tiendaonlinedamdaw123$";
    $db   = "tiendaonlinedamdaw";

    $conexion = new mysqli($host, $user, $pass, $db);

    $sql = "SELECT * FROM producto;";

    $resultado = $conexion->query($sql);
    while ($fila = $resultado->fetch_assoc()) {
?>
	<article>
  	<div class="imagen"></div>
    <h3><?= $fila['nombre_producto'] ?></h3>
    <p><?= $fila['precio'] ?></p>
    <p><?= $fila['descripcion'] ?></p>
    <a href="comprar.php">Comprar</a>
  </article>
<?php
    }

    $conexion->close();
?>

<?php include "inc/piedepagina.php"; ?>