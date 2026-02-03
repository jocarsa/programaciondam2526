<!doctype html>
<html lang="es">
  <head>
    <title>Tienda</title>
    <meta name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <style>
      /* ===== Mobile-first enhancements ===== */
@media (max-width: 768px){

  body{
    font-size:16px;
  }

  header h1{
    margin:0;
    font-size:1.4rem;
  }

  main{
    padding:10px;
  }

  section{
    margin-bottom:20px;
  }

  h3{
    margin-bottom:10px;
    font-size:1.2rem;
    text-align:center;
  }

  /* Products layout */
  #productos > div{
    display:flex;
    flex-direction:column;
    gap:12px;
  }

  article{
    border:1px solid #ddd;
    padding:12px;
    border-radius:8px;
    display:flex;
    justify-content:space-between;
    align-items:center;
  }

  article h4{
    margin:0;
    font-size:1rem;
  }

  button{
    padding:10px 14px;
    font-size:1rem;
    border:none;
    border-radius:6px;
    background:#000;
    color:#fff;
    cursor:pointer;
  }

  button:active{
    transform:scale(0.97);
  }

  /* Client data form */
  section:last-of-type > div{
    display:flex;
    flex-direction:column;
    gap:10px;
  }

  input{
    padding:10px;
    font-size:1rem;
    border-radius:6px;
    border:1px solid #ccc;
    width:100%;
    box-sizing:border-box;
  }

  #enviar{
    margin-top:10px;
    padding:12px;
    text-align:center;
    background:#000;
    color:#fff;
    border-radius:8px;
    font-size:1rem;
    cursor:pointer;
  }

  #enviar:active{
    transform:scale(0.98);
  }

  footer{
    font-size:0.85rem;
    padding:8px;
  }
}

    </style>
    <meta charset="utf-8">
  </head>
  <body>
    <header>
      <h1>Microtienda</h1>
    </header>
    <main>
      <section id="productos">
        <h3>Productos</h3>
        <div>
          <?php
            $host = "localhost";
            $user = "microtienda";
            $pass = "Microtienda123$";
            $db   = "microtienda";
            $conexion = new mysqli($host, $user, $pass, $db);
            $sql = "SELECT * FROM productos;";
            $resultado = $conexion->query($sql);
            while ($fila = $resultado->fetch_assoc()) {
          ?>
            <article>
              <h4><?= $fila['nombre'] ?></h4>
              <button nombre="<?= $fila['nombre'] ?>"><?= $fila['precio'] ?>€</button>
            </article>
          <?php }?>
        </div>
      </section>
      <section>
        <h3>Datos de cliente</h3>
        <div>
          <input type="text" id="nombre" placeholder="Nombre">
          <input type="text" id="apellidos" placeholder="Apellidos">
          <input type="text" id="email" placeholder="Email">
          <div id="enviar">Enviar pedido</div>
        </div>
      </section>
    </main>
    <footer>
      (c) 2026 Jose Vicente Carratala
    </footer>
  </body>
  <script>
    var fecha = new Date();
    var pedido = {
    	cliente:{},
      productos:[],
      pedido:{
      	"numero":Date.now(),
        "fecha":fecha.getFullYear()+"-"+(fecha.getMonth()+1)+"-"+fecha.getDate()
      }
    };
    /////// Atrapa productos y los mete en el carro
    let botones = document.querySelectorAll("button");
    botones.forEach(function(boton){
    	boton.onclick = function(){
      	pedido.productos.push({
          "nombre":this.getAttribute("nombre"),
        	"precio":this.textContent
        })
        console.log(pedido)
      }
    })
    console.log(pedido)
    /////// Atrapa los datos del cliente
    let boton_enviar = document.querySelector("#enviar");
    boton_enviar.onclick = function(){
      let nombre_cliente = document.querySelector("#nombre").value;
      let apellidos_cliente = document.querySelector("#apellidos").value;
      let email_cliente = document.querySelector("#email").value;
      pedido.cliente = {
        "nombre":nombre_cliente,
        "apellidos":apellidos_cliente,
        "email":email_cliente
      }
      console.log(pedido)
      // Y los envio para guardar
      fetch("guardamongo.php", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(pedido)
});
    }
  </script>
</html>