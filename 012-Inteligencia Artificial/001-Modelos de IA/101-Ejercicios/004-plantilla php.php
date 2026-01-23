<?php

// sudo apt install php php-curl
// sudo service apache2 restart

$OLLAMA_URL = "http://localhost:11434/api/generate";
$MODEL = "qwen2.5:3b-instruct";

$prompt = "Explica qué es PHP.";

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
