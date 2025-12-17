<?php
	$sql = "INSERT INTO ".$_GET['tabla']." VALUES (";	// Inicio el formateo del SQL
  foreach($_POST as $clave=>$valor){							// Recorro los campos del form
  	if($clave == "id"){														// Si eres un id
    	$sql.= "NULL,";															// Inserta NULL
    }else{																				// Si no eres un id
  		$sql.= "'".$valor."',";											// Inserta el valor
    }
  }
  
  $sql = substr($sql, 0, -1); // Le quito la ultima coma al SQL	// Le quito la coma
  $sql .= ");";
  echo $sql;																			// Lo saco por pantalla
  
  $resultado = $conexion->query($sql);						// Proceso el SQL
  header("Location: ?tabla=".$_GET['tabla']);
?>