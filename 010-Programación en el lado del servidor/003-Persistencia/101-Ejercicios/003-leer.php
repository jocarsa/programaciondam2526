<?php
  $archivo = fopen("archivo.txt", "r"); // "r" = leer/read
  
  // Parámetros 1.-Lo que lees 2.-Longitud de lo que lees
  $contenido = fread($archivo,filesize("archivo.txt"));
  
  echo $contenido;
  fclose($archivo);
?>