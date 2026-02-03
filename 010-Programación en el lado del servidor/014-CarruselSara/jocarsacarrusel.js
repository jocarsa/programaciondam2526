// Cojo el contenedor externo (es un solo elemento)
      let contenedor = document.querySelector(".jocarsacarrusel");
      // Cojo las imagenes de dentro (es un array de elementos)
      let contenido = document.querySelectorAll(".jocarsacarrusel img")
      // Para cada una de las imagenes
      contenido.forEach(function(elemento){
        // Quito la imagen del html
      	elemento.remove()
      })
      // Creo un nuevo contenedor que es una seccion
      let nuevo_contenedor = document.createElement("section")
      nuevo_contenedor.style.left = 0
      // Al contenedor antiguo le añado el nuevo contenedor
      contenedor.appendChild(nuevo_contenedor)
      
      // Dentro del nuevo contenedor meto las imagenes una a una
      contenido.forEach(function(elemento){
      	nuevo_contenedor.appendChild(elemento)
      })
      // Ahora creo dos botones
      let botonatras = document.createElement("button")
      botonatras.textContent = "◀"
      contenedor.appendChild(botonatras)
      let botondelante = document.createElement("button")
      botondelante.textContent = "▶"
      contenedor.appendChild(botondelante)
      var anchura = 1280;
      var contador = 0;
      // Cuando haga click en el boton delante
      botondelante.onclick = function(){
        // Le quito un elemento al contador
        console.log(contador)
        contador--;
        if(contador < -7){contador = 0;}
        // Actualizo la posicion del nuevo contenedor
      	nuevo_contenedor.style.left = contador*anchura+"px"
      }
      // Cuando haga click en el boton atras
      botonatras.onclick = function(){
        // Le quito un elemento al contador
        console.log(contador)
        contador++;
        if(contador > 0){contador = 0;}
        // Actualizo la posicion del nuevo contenedor
      	nuevo_contenedor.style.left = contador*anchura+"px"
      }