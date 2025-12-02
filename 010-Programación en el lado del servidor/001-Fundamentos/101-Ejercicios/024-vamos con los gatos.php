<?php

	class Gato{
  	function __construct($color,$edad){
    	$this->color = $color;
      $this->edad = $edad;
    }
  }
  
  $gato1 = new Gato("Naranja",1);
  $gato2 = new Gato("Blanco",2);
  
  var_dump($gato1);

?>