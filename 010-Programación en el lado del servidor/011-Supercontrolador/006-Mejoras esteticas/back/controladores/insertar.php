<form action="?operacion=procesainsertar&tabla=<?= $_GET['tabla'] ?>" method="POST">
<?php
      // CREAMOS UN FORMULARIO DINÁMICO
      
        $resultado = $conexion->query("
          SELECT * FROM ".$_GET['tabla']." LIMIT 1;
        ");	// SOLO QUIERO UN ELEMENTO !!!!!!!!!!!!!!!!
        while ($fila = $resultado->fetch_assoc()) {
          foreach($fila as $clave=>$valor){
            echo "
            	<div class='control_formulario'>
                <label>".$clave."</label>
                <input 
                  type='text' 
                  name='".$clave."'
                  placeholder='".$clave."'>
              </div>
              ";
          }
         }
      ?>
   <div class='control_formulario'>
   	<label>Insertar</label>
     <input type="submit">
   </div>
</form>
<style>
	form{
  	width:100%;
    display:flex;
    flex-direction:column;
    gap:20px;
  }
  .control_formulario{
  	display:flex;
  }
  label{
  	flex:1;
  }
  input{
  	flex:4;
    padding:10px;
    border:2px solid plum;
  }
  input[type=submit]{
  	background:plum;
    color:white;
  }
</style>




