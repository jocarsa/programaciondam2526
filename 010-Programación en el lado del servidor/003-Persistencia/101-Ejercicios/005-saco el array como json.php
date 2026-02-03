<?php
  $cliente = [];
  $cliente['nombre'] = "Jose Vicente";
  $cliente['apellidos'] = "Carratala Sanchis";
  $cliente['email'] = "info@jocarsa.com";
  
  $json = json_encode($cliente);
  echo $json;  
?>