<table>
      <?php
      // PRIMERO CREO LAS CABECERAS //////////////////
        $resultado = $conexion->query("
          SELECT * FROM ".$_GET['tabla']." LIMIT 1;
        ");	// SOLO QUIERO UN ELEMENTO !!!!!!!!!!!!!!!!
        while ($fila = $resultado->fetch_assoc()) {
          echo "<tr>";
          foreach($fila as $clave=>$valor){
            echo "<th>".$clave."</th>";		// En lugar de enseñarme el valor, enseñame la clave
          }
          echo "</tr>";
         }
      ?>
      <?php
      // Y LUEGO EL RESTO DE DATOS //////////////
        $resultado = $conexion->query("
          SELECT * FROM ".$_GET['tabla'].";
        ");
        while ($fila = $resultado->fetch_assoc()) {
          echo "<tr>";
          foreach($fila as $clave=>$valor){
            echo "<td>".$valor."</td>";
          }
          echo "</tr>";
         }
      ?>
</table>
<!-- Me voy a la operacion insertar y me llevo la tabla actual -->
<a href="?operacion=insertar&tabla=<?= $_GET['tabla'] ?>" class="boton_insertar">+</a>
<style>
	.boton_insertar{
  	position:absolute;
    bottom:20px;
    right:20px;
    background:plum;
    border-radius:30px;
    width:30px;
    height:30px;
    color:white;
    text-align:center;
    line-height:30px;
    text-decoration:none;
  }
</style>





