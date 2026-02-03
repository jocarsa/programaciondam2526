<!doctype html>
<html>
	<head>
  	<style>
    	html,body{padding:0px;margin:0px;width:100%;height:100%;}
      body{display:flex;}
      nav{flex:1;background:coral;color:white;display:flex;flex-direction:column;
      gap:10px;padding:10px;}
      main{flex:5;padding:10px;display:flex;}
      nav a{background:white;color:coral;padding:10px;}
      main table{flex:1;border:2px solid coral;}
      main table thead{background:coral;color:white;}
      main form{flex:1;}
    </style>
  </head>
  <body>
  	<nav>
    	<a>Viviendas</a>
      <a>Imagenes</a>
      <a>Usuarios</a>
      <a>Propietarios</a>
      <a>Alquileres</a>
      <a>a</a>
      <a>b</a>
      <a>c</a>
      <a>d</a>
      <a>e</a>
    </nav>
    <main>
    	<table>
      	<thead>
        	<tr>
          	<th>localidad</th>
            <th>precio</th>
            <th>metroscuadrados</th>
            <th>aniodeconstruccion</th>
            <!--
            <th>direccion</th>
            <th>altura</th>
            <th>tipodevivienda</th>
            <th>descripcion</th>
            <th>estado</th>
            <th>banios</th>
            <th>habitaciones</th>
            <th>teniente</th>
            -->
          </tr>
        </thead>
        <tbody>
        	<?php
            $host = "localhost";
            $user = "camaron";
            $pass = "Camaron123$";
            $db   = "camaron";

            $conexion = new mysqli($host, $user, $pass, $db);
            $resultado = $conexion->query("
              SELECT * FROM viviendas 
              ;
            ");
            while ($fila = $resultado->fetch_assoc()) {
            	echo '<tr>
              	<td>'.$fila['localidad'].'</td>
                <td>'.$fila['precio'].'</td>
                <td>'.$fila['metroscuadrados'].'</td>
                <td>'.$fila['aniodeconstruccion'].'</td>
                
              </tr>';
              /*<td>'.$fila['direccion'].'</td>
                <td>'.$fila['altura'].'</td>
                <td>'.$fila['tipodevivienda'].'</td>
                <td>'.$fila['descripcion'].'</td>
                <td>'.$fila['estado'].'</td>
                <td>'.$fila['banios'].'</td>
                <td>'.$fila['habitaciones'].'</td>
                <td>'.$fila['teniente'].'</td> */
            }
        	?>
        </tbody>
      </table>
      <form>
      </form>
    </main>
  </body>
</html>