<!doctype html>
<html>
	<head>
  	<style>
    	.dia{border:1px solid black;padding:10px;width:50px;
      height:50px;display:inline-block;}
    </style>
  </head>
  <body>
    <?php
      // El signo de encadenamiento es el . (y eso es superguay)

      for($dia = 1;$dia < 31;$dia++){
        echo "<div class='dia'>".$dia."</div>";
      }
    ?>
  </body>
</html>