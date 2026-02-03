<?php
      // Ahora lo que quiero es un listado de las tablas en la base de datos
        $resultado = $conexion->query("
          SHOW TABLES;
        ");
        while ($fila = $resultado->fetch_assoc()) {
          echo '<a href="?tabla='.$fila['Tables_in_'.$db].'">'.$fila['Tables_in_'.$db].'</a>';
        }
    ?>