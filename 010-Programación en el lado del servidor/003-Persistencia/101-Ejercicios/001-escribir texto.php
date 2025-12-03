<?php
  $archivo = fopen("archivo.txt", "a"); // "a" = append
  fwrite($archivo, "Nuevo texto escrito desde PHP\n");
  fclose($archivo);
?>