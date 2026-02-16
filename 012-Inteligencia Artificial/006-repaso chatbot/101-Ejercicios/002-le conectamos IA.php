<!doctype html>
<html>
  <head>
    <style>
      html,body{margin:0px;padding:0px;width:100%;height:100%;}
      body{display:flex;justify-content:center;align-items:center;}
      form{border:1px solid lightgrey;padding:20px;border-radius:10px;
      height:300px;width:300px;display:flex;flex-direction:column;
      gap:20px;}
      input{padding:10px;}
      input[type=text]{background:yellow;border-radius:10px 0px 10px 10px;}
      p{padding:10px;background:lightgreen;border-radius:0px 10px 10px 10px;}
    </style>
  </head>
  <body>
    <form action="?" method="POST">
      <p>
      	<?php
          $OLLAMA_URL = "http://localhost:11434/api/generate";
          $MODEL = "qwen2.5-coder:7b";
          $prompt = $_POST['mensaje'];
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
      </p>
      <input type="text" name="mensaje">
      <input type="submit">
    </form>
  </body>
</html>