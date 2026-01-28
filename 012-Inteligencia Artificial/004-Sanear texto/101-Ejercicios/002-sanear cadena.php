<?php

// sudo apt install php php-curl
// sudo service apache2 restart

$OLLAMA_URL = "http://localhost:11434/api/generate";
$MODEL = "qwen2.5:3b-instruct";

$prompt = "Sanea la siguiente cadena, 
	- pon comas, 
  - puntos, 
  - separa en frases,
	- y si es necesario, separa en párrafos si existen diferentes temas. 
  
  -Devuelve frases y párrafos en HTML usando la etiqueta <p>, pon <br> al final de cada linea, y doble <br> al final de cada parrafo
  -Detecta las cuatro palabras mas importantes de cada parrafo, y ponlas en negrita con la etiqueta <b> de HTML
  -Pon en mayúsculas la primera letra de cada frase o párrafo
  
  La cadena es:
  ahora a continuación lo que quiero al menos en mi objetivo para la clase de hoy es montar este bloque el bloque motor montar la placa de control montar en ultrasonidos y comprobar como el robot hace algo cuando digo algo lo que quiero decir es que mediante el ultrasonido es por ejemplo lo que quiero es que detecte lo que tiene delante y si detecta algún obstáculo pues por ejemplo que se pare es decir quiero empezar a hacer algo empezar a unir los componentes y que se vea como la unión de los componentes realmente nos permiten construir algo de utilidad enfocar lo que me interesa lo que podemos ir haciendo mientras tanto es ir preparando el sketch así dejamos que el pegamento vaya haciendo su labor y no te digo lo que podemos hacer es ir abriendo el proyecto de arduino e ir configurando lo y así también de paso vamos hablando de la programación y así también le damos tiempo al pegamento para que se acabe de unir y evidentemente para esto lo que voy a hacer es reutilizar gran parte del código que hemos utilizado en días anteriores pues no va a ser un proyecto desde cero sino que vamos a copiar y pegar código de días anteriores vale tenemos esto y a continuación voy a abrir y voy a abrir un proyecto por ejemplo por una parte de bueno fíjate vamos a abrir pero dónde estás servo 360 vamos a abrir ultrasonidos y vamos a abrir está un poco más ultrasonidos y servo pues todos los ejercicios que hemos hecho hasta ahora realmente son ejercicios que nos van a servir para diseñar combinando el código entre sí otros ejercicios voy a esto archivo guardar como no voy a guardar en curso arduino con el nombre de 30 24 robot ultrasonidos y ahora lo que hago es copiar y pegar esto es ultrasonidos pues no quería yo quería de hecho el servomotor muy bien incluyó el serbo copio y pego creó un servo de hecho el que ya hemos comentado anteriormente el código viene bien porque así sabemos qué es lo que ocurre en cada caso y ahora motor punto a touch a los puertos antes hemos dicho que voy a utilizar el 7 y el entonces claro tengo que hacer servo motor derecho y cervo motor izquierdo motor derecho a touch voy a decir de momento el número 8 y motor izquierdo va touch el puerto 7 hemos dicho 1 767 heces ahora lo que voy a
  ";

$data = [
    "model" => $MODEL,
    "prompt" => $prompt,
    "stream" => false
];

$ch = curl_init($OLLAMA_URL);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json"
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

$response = curl_exec($ch);

if ($response === false) {
    die("cURL error: " . curl_error($ch));
}

curl_close($ch);

$result = json_decode($response, true);

echo $result["response"];
