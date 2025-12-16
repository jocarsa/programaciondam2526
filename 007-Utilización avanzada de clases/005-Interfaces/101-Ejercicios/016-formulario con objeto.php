<?php
	
  $cliente = [
  	"nombre" => "Jose Vicente",
    "apellidos" => "Carratala Sanchis",
    "email" => "info@jocarsa.com"
  ];
  
  foreach($cliente as $clave=>$valor){
  	echo "<label>".$clave."</label>";
    echo "<input type='text' value='".$valor."'>";
  }
 
?>