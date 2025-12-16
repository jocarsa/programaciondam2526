<?php
	
  $campos_cliente = [
  	"nombre",
    "apellidos",
    "email",
    "telefono",
    "direccion"
  ];
  
  foreach($campos_cliente as $campo){
  	echo $campo."<br>";
  }

?>