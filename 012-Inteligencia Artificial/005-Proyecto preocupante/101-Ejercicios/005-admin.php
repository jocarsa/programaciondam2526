<?php

// sudo apt install php php-curl
// sudo service apache2 restart

$OLLAMA_URL = "http://localhost:11434/api/generate";
$MODEL = "qwen2.5-coder:7b";

$prompt = "
  Inventa un conjunto de datos. Forma tabular.
  Crea una tabla HTML y CSS para representar esos datos.
  Hazla bonita con CSS.
  Crea un solo archivo single file html para presentar esa información en pantalla.
  No des explicaciones, solo quiero el codigo puro, sin fences.
  Mediante Javascript, haz que la tabla sea reordenable (sortable) haciendo click en las cabeceras.
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

echo $result["response"];
