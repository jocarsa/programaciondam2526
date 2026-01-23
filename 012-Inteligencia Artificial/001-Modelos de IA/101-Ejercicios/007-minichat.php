<!doctype html>
<html>
	<head>
  	<style>
    	html,body{padding:0px;margin:0px;width:100%;height:100%;}
      body{display:flex;justify-content:center;align-items:center;}
      main{width:500px;height:500px;padding:20px;border:1px solid grey;
      border-radius:5px;display:flex;flex-direction:column;justify-content:space-between;}
      input{width:100%;padding:10px;box-sizing:border-box;}
      article{background:lightgreen;padding:20px;border-radius:10px 0px 10px 10px;}
    </style>
  </head>
  <body>
  	<main>
    	<section>
      	<article>
        	<?php echo $_POST['mensaje'] ?>
        </article>
      </section>
      <form action="?" method="POST">
      <input type="text" name="mensaje">
      </form>
    </main>
  </body>
</html>