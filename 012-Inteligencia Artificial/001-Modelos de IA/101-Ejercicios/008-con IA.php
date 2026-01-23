<!doctype html>
<html>
	<head>
  	<style>
    	html,body{padding:0px;margin:0px;width:100%;height:100%;font-family:ubuntu;}
      body{display:flex;justify-content:center;align-items:center;}
      main{width:500px;height:500px;padding:20px;border:1px solid grey;
      border-radius:5px;display:flex;flex-direction:column;justify-content:space-between;}
      input{width:100%;padding:10px;box-sizing:border-box;background:yellow;border:none;
      border-radius:0px 10px 10px 10px;}
      article{background:lightgreen;padding:20px;border-radius:10px 0px 10px 10px;
      text-aling:justify;}
    </style>
  </head>
  <body>
  	<main>
    	<section>
      	<article>
        	<?php
            $OLLAMA_URL = "http://localhost:11434/api/generate";
            $MODEL = "qwen2.5:3b-instruct";
            $prompt = $_POST['mensaje'].". Responde en español.";
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
            echo $_POST['mensaje']."<br>".$result["response"];
          ?>
        </article>
      </section>
      <form action="?" method="POST">
      <input type="text" name="mensaje">
      </form>
    </main>
  </body>
</html>