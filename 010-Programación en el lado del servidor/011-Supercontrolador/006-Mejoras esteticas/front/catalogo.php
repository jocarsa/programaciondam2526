<?php include "inc/cabecera.php"; ?>

<section id="catalogo">

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
        <div class="imagen" style="background:url(img/producto.jpg);background-size:cover;"></div>
        <h3><?= $fila['nombre_producto'] ?></h3>
        <p><?= $fila['precio'] ?></p>
        <p><?= $fila['descripcion'] ?></p>
        <a href="producto.php?id=<?= $fila['id'] ?>">Comprar</a> <!-- NUEVO -->
      </article>
    <?php
        }

        $conexion->close();
    ?>

</section>

<style>
	#catalogo{
  	display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:20px;
  }
  #catalogo article{
  	text-align:center;
  }
  #catalogo article .imagen{
  	background:darkorchid;
    height:100px;
    border-radius:5px 5px 0px 0px;
  }
  #catalogo article a{
  	background:darkorchid;
    padding:10px;
    border-radius:5px;
    color:white;
    text-decoration:none;
  }
</style>

<?php include "inc/piedepagina.php"; ?>



