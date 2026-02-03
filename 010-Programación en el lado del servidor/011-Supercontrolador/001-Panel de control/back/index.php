<!doctype html>
<html>
	<head>
  	<style>
    	html,body{width:100%;height:100%;padding:0px;margin:0px;}
      body{display:flex;font-family:sans-serif;}
      nav{background:plum;padding:20px;gap:20px;flex:1;
      display:flex;flex-direction:column;gap:20px;}
      nav a{background:white;color:plum;text-decoration:none;
      padding:10px;}
      main{padding:20px;flex:4;}
      table td{padding:10px;}
      table{border:2px solid plum;width:100%;}
      th{background:plum;color:white;padding:10px;}
    </style>
  </head>
  <body>
    <?php
      // Primero me conecto a la base de datos
      // Esto es común para todo el archivo
        $host = "localhost";
        $user = "tiendaonlinedamdaw";
        $pass = "Tiendaonlinedamdaw123$";
        $db   = "tiendaonlinedamdaw";

        $conexion = new mysqli($host, $user, $pass, $db);
    ?>

    <nav>
    <?php
      // Ahora lo que quiero es un listado de las tablas en la base de datos
        $resultado = $conexion->query("
          SHOW TABLES;
        ");
        while ($fila = $resultado->fetch_assoc()) {
          echo '<a href="?tabla='.$fila['Tables_in_'.$db].'">'.$fila['Tables_in_'.$db].'</a>';
        }
    ?>
    </nav>
    <main>
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
    </main>
  </body>
</html>