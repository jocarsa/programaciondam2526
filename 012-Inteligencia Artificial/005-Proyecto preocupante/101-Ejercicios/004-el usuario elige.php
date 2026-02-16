<form action="?" method="POST">
	<p>Indica la web que quieres hacer</p>
	<textarea name="descripcion"></textarea>
  <input type="submit">
</form>
<?php
if(isset($_POST['descripcion'])){
  // sudo apt install php php-curl
  // sudo service apache2 restart

  $OLLAMA_URL = "http://localhost:11434/api/generate";
  $MODEL = "qwen2.5-coder:7b";

  $prompt = $_POST['descripcion'];

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
}
?>
