<?php
  $OLLAMA_URL = "http://localhost:11434/api/generate";
  $MODEL = "qwen2.5-coder:7b";
  $prompt = "
  	Tengo una base de datos que tiene una tabla clientes con esta estructura:
    CREATE TABLE clientes (
      id INT(11) NOT NULL AUTO_INCREMENT,
      nombre VARCHAR(255),
      apellidos VARCHAR(255),
      email VARCHAR(255),
      poblacion VARCHAR(255),
      fecha_de_nacimiento DATE,
      PRIMARY KEY (id)
  );
  Lo que quiero es que me des el SQL para responder a
  la siguiente petición por parte del usuario:
  Dame todos los clientes que vivan en Valencia.
  Lo que necesito es que me des el codigo SQL para esa peticion.
  No me des nada más que código SQL. Tampoco quiero fences.
  Cuando hagas consultas con Where, usa WHERE x LIKE '%y%'.
  El codigo resultante debe ser SQL puro, nunca markdown.
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
  curl_close($ch);
  $result = json_decode($response, true);
  echo @$result["response"];
?>