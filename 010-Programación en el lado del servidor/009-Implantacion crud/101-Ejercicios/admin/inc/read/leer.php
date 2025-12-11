<table>
  <?php
    $host = "localhost";
    $user = "periodico";
    $pass = "Periodico123$";
    $db   = "periodico";

    $conexion = new mysqli($host, $user, $pass, $db);

    $sql = "SELECT * FROM noticias;";

    $resultado = $conexion->query($sql);
    while ($fila = $resultado->fetch_assoc()) {
			echo "<tr>";
      	echo "<td>".$fila['titulo']."</td>";
        echo "<td>".$fila['fecha_publicacion']."</td>";
        echo "<td>".$fila['autor_id']."</td>";
        echo "<td>".$fila['contenido']."</td>";
      echo "</tr>";
    }

    $conexion->close();
  ?>
</table>