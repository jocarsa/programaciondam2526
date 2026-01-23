<!doctype html>
<html>
	<head>
  	<style>
    	body,html{padding:0px;margin:0px;width:100%;height:100%;}
      body{display:flex;justify-content:center;align-items:center;}
      main{width:600px;height:400px;background:black;color:white;border-radius:5px;padding:20px;
      font-family:monospace;text-align:justify;box-shadow:0px 5px 10px rgba(0,0,0,.4);}
    </style>
  </head>
  <body>
  <main>
    <?php
      $OLLAMA_URL = "http://localhost:11434/api/generate";
      $MODEL = "qwen2.5:3b-instruct";
      $prompt = "Dime quién es Jose Vicente Carratalá. Responde en español.";
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
    ?>
  </main>
</html>