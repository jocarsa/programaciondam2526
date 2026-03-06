En primer lugar, vamos a crear un mini-servidor
específicamente para este ejercicio

Va a ser un mini-servidor Ubuntu Server 24.04LTS

Lo que quiero es que creéis un máquina nueva
Porque NGINX se va a pegar de leches con Apache

1.-Descargad o reutilizad la imagen ISO de Ubuntu Server
2.-Creamos una máquina no muy potente:
-2-4 nucleos
-2-4 GB RAM
-120GB de disco
-Importante: Red en adaptador puente desde el principio

Cambio de idea:
En un entorno ideal, instalaríamos Ubuntu Server para 
probar "la experiencia real"

Pero ahora mismo tenemos problemas en la red del aula
Una forma de sortear los problemas es instalar un Ubuntu normal
Que tenga tanto servidor como interfaz de usuario y navegador web
Para poder probar lo que vamos a hacer sin depender de la red
(o sea, en local)

Entonces, instalamos una máquina nueva o reusamos la que tenéis:
1.-Si usáis una nueva, es un rollo porque la tenéis que configurar
Pero lo que instaléis no se va a pegar con lo que tengáis
2.-Si reusáis, lo que instaléis se pegará con lo que ya tenéis
Con lo cual tendréis que apagar cosas

2.-Creamos una máquina un poco potente:
-4-8 nucleos
-4-8 GB RAM
-120GB de disco
-Importante: Red en adaptador puente desde el principio
-Red en adaptador puente

3.-Es recomendable (especialmente en Ubuntu Desktop)
que instaléis las Virtual Box Tools (nos permiten copiar y pegar,
reescalar pantalla, etc etc) - es lo mismo que las Guest Additions
Dispositivos - Insertar el CD con los complementos de invitado

https://download.virtualbox.org/virtualbox/