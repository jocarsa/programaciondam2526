<?php include "inc/cabecera.php"; ?>

<section id="paginaproducto">

    <?php
      $host = "localhost";
      $user = "tiendaonlinedamdaw";
      $pass = "Tiendaonlinedamdaw123$";
      $db   = "tiendaonlinedamdaw";

      $conexion = new mysqli($host, $user, $pass, $db);

      $sql = "SELECT * FROM producto WHERE id = ".$_GET['id'].";"; // NUEVO ///////////

      $resultado = $conexion->query($sql);
      while ($fila = $resultado->fetch_assoc()) {
    ?>
      <article>
        <div class="imagen" style="background:url(img/producto.jpg);background-size:cover;"></div>
        <p><?= $fila['precio'] ?></p>
        <form action="carrito.php" method="POST">
        	<input type="hidden" name="id" value="<?= $fila['id'] ?>">
          <input type="number" name="unidades" min=1 max=10 value=1>
          <input type="submit" value="Comprar">
        </form>
      </article>
      <article>
      	<h3><?= $fila['nombre_producto'] ?></h3>
        <h4><?= $fila['descripcion'] ?></h4>
        <p><?= $fila['descripcion_larga'] ?></p>
      </article>
    <?php
        }

        $conexion->close();
    ?>

</section>

<style>
	#paginaproducto{
  	display:flex;
    gap:20px;
  }
  #paginaproducto article{
  	text-align:justify;
    flex:1;
  }
  #paginaproducto article .imagen{
  	background:darkorchid;
    height:300px;
    border-radius:5px 5px 0px 0px;
  }
  #paginaproducto article a{
  	background:darkorchid;
    padding:10px;
    border-radius:5px;
    color:white;
    text-decoration:none;
  }
</style>

<?php include "inc/piedepagina.php"; ?>



