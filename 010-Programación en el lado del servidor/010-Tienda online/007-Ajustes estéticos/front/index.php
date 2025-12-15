<?php include "inc/cabecera.php"; ?>

<section id="heroe">
	<h3>Motivo por el cual debería comprar</h3>
  <p>Frase sugerente al respecto</p>
  <a href="catalogo.php">Vamos a ver esa maravilla de catálogo</a>
</section>
<style>
	#heroe{
  	background:darkorchid;
    height:400px;
    display:flex;
    flex-direction:column;
    color:white;
    justify-content:center;
    align-items:center;
    border-radius:5px;
    margin-bottom:20px;
  }
  #heroe a{
  	color:darkorchid;
    background:white;
    text-decoration:none;
    padding:10px;
    border-radius:5px;
  }
</style>
<section id="razones">
	<article>
  	<h4>Razon 1 por la cual debes comprar</h4>
    <p>Descripción de esa razón</p>
  </article>
  <article>
  	<h4>Razon 2 por la cual debes comprar</h4>
    <p>Descripción de esa razón</p>
  </article>
  <article>
  	<h4>Razon 3 por la cual debes comprar</h4>
    <p>Descripción de esa razón</p>
  </article>
  <article>
  	<h4>Razon 4 por la cual debes comprar</h4>
    <p>Descripción de esa razón</p>
  </article>
</section>
<style>
	#razones{
  	display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:20px;
  }
  #razones article{
  	text-align:center;
    background:darkorchid;
    padding:20px;
    border-radius:5px;
    display:flex;
    flex-direction:column;
    color:white;
    justify-content:center;
    align-items:center;
  }
  
</style>

<?php include "inc/piedepagina.php"; ?>