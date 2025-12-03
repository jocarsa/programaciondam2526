<?php
	echo 4 == 4 && 3 == 3 && 2 == 2; // Verdadero
  echo 4 == 4 && 3 == 3 && 2 == 1; // Falso
  
  echo 4 == 4 || 3 == 3 || 2 == 2; // Verdadero
  echo 4 == 4 || 3 == 3 || 2 == 1; // Verdadero
  echo 4 == 4 || 3 == 2 || 2 == 1; // Verdadero
  echo 4 == 3 || 3 == 2 || 2 == 1; // Falso
?>