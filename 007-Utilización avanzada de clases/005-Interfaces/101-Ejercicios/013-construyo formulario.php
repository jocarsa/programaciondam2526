<?php
	
  $campos_cliente = [
  	"nombre",
    "apellidos",
    "email",
    "telefono",
    "direccion",
    "poblacion"
  ];
  
  foreach($campos_cliente as $campo){
  	echo '<input type="text" placeholder="'.$campo.'"><br>';
  }

?>