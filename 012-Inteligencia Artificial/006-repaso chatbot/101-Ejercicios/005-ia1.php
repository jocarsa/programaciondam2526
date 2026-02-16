<?php
session_start();

// Si no existe, creo memoria de preguntas y respuestas
if (!isset($_SESSION['preguntas'])) { $_SESSION['preguntas'] = []; }
if (!isset($_SESSION['respuestas'])) { $_SESSION['respuestas'] = []; }

$OLLAMA_URL = "http://localhost:11434/api/generate";
$MODEL = "qwen2.5-coder:7b";

// Procesar envío
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["mensaje"])) {
  $mensaje = trim($_POST["mensaje"]);

  if ($mensaje !== "") {
    // Envio la pregunta a la IA
    $prompt = $mensaje . ". Resume tu respuesta en una unica frase";
    $data = [
      "model" => $MODEL,
      "prompt" => $prompt,
      "stream" => false
    ];

    $ch = curl_init($OLLAMA_URL);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: application/json"]);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    $response = curl_exec($ch);
    curl_close($ch);

    $result = json_decode($response, true);
    $respuesta = isset($result["response"]) ? $result["response"] : "No se pudo obtener respuesta.";

    // Guardar en sesión
    $_SESSION['preguntas'][] = $mensaje;
    $_SESSION['respuestas'][] = $respuesta;
  }

  // Evitar reenvío al recargar
  header("Location: " . strtok($_SERVER["REQUEST_URI"], "?"));
  exit;
}
?>
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Chat (Ollama)</title>
  <style>
    :root{
      --bg: #f6f7fb;
      --card: #ffffff;
      --border: #e7e9f2;
      --text: #111827;
      --muted: #6b7280;

      --bubble-user: #dcf8c6;   /* WhatsApp-like */
      --bubble-ai:   #ffffff;
      --bubble-ai-border: #eef0f6;

      --input-bg: #ffffff;
      --focus: #2563eb;

      --shadow: 0 14px 34px rgba(17, 24, 39, 0.10);
    }

    *{ box-sizing: border-box; }
    html, body{ height:100%; }

    body{
      margin:0;
      background: var(--bg);
      color: var(--text);
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, "Helvetica Neue", Arial;
      display:flex;
      align-items:center;
      justify-content:center;
      padding: 20px;
    }

    .app{
      width: min(720px, 100%);
      height: min(820px, 100%);
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 18px;
      box-shadow: var(--shadow);
      display:flex;
      flex-direction: column;
      overflow: hidden;
    }

    .header{
      padding: 14px 16px;
      border-bottom: 1px solid var(--border);
      display:flex;
      align-items:center;
      justify-content: space-between;
      gap: 12px;
    }

    .title{
      display:flex;
      flex-direction: column;
      gap: 2px;
      min-width: 0;
    }

    .title strong{
      font-size: 14px;
      line-height: 1.1;
    }

    .title span{
      font-size: 12px;
      color: var(--muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .chat{
      flex: 1;
      padding: 16px 14px;
      overflow-y: auto;
      background:
        radial-gradient(circle at 20px 20px, rgba(17,24,39,0.03) 0 1px, transparent 1px 100%),
        radial-gradient(circle at 60px 60px, rgba(17,24,39,0.02) 0 1px, transparent 1px 100%);
      background-size: 80px 80px;
    }

    .row{
      display:flex;
      margin: 10px 0;
    }

    .row.user{ justify-content: flex-end; }
    .row.ai{ justify-content: flex-start; }

    .bubble{
      max-width: 78%;
      padding: 10px 12px;
      border-radius: 16px;
      line-height: 1.35;
      font-size: 14px;
      word-wrap: break-word;
      position: relative;
    }

    /* Globo usuario (derecha) */
    .bubble.user{
      background: var(--bubble-user);
      border-top-right-radius: 6px;
      box-shadow: 0 6px 14px rgba(17, 24, 39, 0.06);
    }
    .bubble.user::after{
      content:"";
      position:absolute;
      right:-6px;
      bottom:10px;
      width: 0;
      height: 0;
      border-left: 8px solid var(--bubble-user);
      border-top: 8px solid transparent;
      border-bottom: 8px solid transparent;
    }

    /* Globo IA (izquierda) */
    .bubble.ai{
      background: var(--bubble-ai);
      border: 1px solid var(--bubble-ai-border);
      border-top-left-radius: 6px;
      box-shadow: 0 6px 14px rgba(17, 24, 39, 0.05);
    }
    .bubble.ai::after{
      content:"";
      position:absolute;
      left:-7px;
      bottom:10px;
      width: 0;
      height: 0;
      border-right: 8px solid var(--bubble-ai);
      border-top: 8px solid transparent;
      border-bottom: 8px solid transparent;
      /* borde sutil del “pico” */
      filter: drop-shadow(-1px 0 0 var(--bubble-ai-border));
    }

    .footer{
      padding: 12px;
      border-top: 1px solid var(--border);
      background: var(--card);
    }

    form{
      display:flex;
      gap: 10px;
      align-items: stretch;
    }

    input[type="text"]{
      flex: 1;
      padding: 12px 12px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: var(--input-bg);
      outline: none;
      font-size: 14px;
    }

    input[type="text"]::placeholder{
      color: var(--muted);
    }

    input[type="text"]:focus{
      border-color: var(--focus);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.14);
    }

    button{
      padding: 12px 14px;
      border-radius: 12px;
      border: 1px solid #cfd5e6;
      background: #ffffff;
      cursor: pointer;
      font-weight: 700;
      min-width: 110px;
      transition: transform .05s ease, box-shadow .15s ease, border-color .15s ease;
    }

    button:hover{
      border-color: #bfc7dd;
      box-shadow: 0 10px 18px rgba(17, 24, 39, 0.06);
    }

    button:active{ transform: translateY(1px); }

    /* Scrollbar discreta */
    .chat::-webkit-scrollbar{ width: 10px; }
    .chat::-webkit-scrollbar-track{ background: transparent; }
    .chat::-webkit-scrollbar-thumb{
      background: #d9deee;
      border-radius: 999px;
      border: 2px solid rgba(0,0,0,0);
      background-clip: padding-box;
    }

    /* móvil */
    @media (max-width: 520px){
      .app{ height: 100%; border-radius: 14px; }
      .bubble{ max-width: 86%; }
      button{ min-width: 90px; }
    }
  </style>
</head>

<body>
  <div class="app">
    <div class="header">
      <div class="title">
        <strong>Chat local (Ollama)</strong>
        <span>Modelo: <?php echo htmlspecialchars($MODEL, ENT_QUOTES, 'UTF-8'); ?></span>
      </div>
      <div style="font-size:12px;color:var(--muted);">
        <?php echo count($_SESSION['preguntas']); ?> turnos
      </div>
    </div>

    <div class="chat" id="chat">
      <?php
        $n = count($_SESSION['preguntas']);
        for ($i = 0; $i < $n; $i++) {
          $q = $_SESSION['preguntas'][$i];
          $a = $_SESSION['respuestas'][$i];

          echo '<div class="row user"><div class="bubble user">' . htmlspecialchars($q, ENT_QUOTES, 'UTF-8') . '</div></div>';
          echo '<div class="row ai"><div class="bubble ai">' . htmlspecialchars($a, ENT_QUOTES, 'UTF-8') . '</div></div>';
        }

        if ($n === 0) {
          echo '<div class="row ai"><div class="bubble ai">Escribe un mensaje para empezar.</div></div>';
        }
      ?>
    </div>

    <div class="footer">
      <form action="?" method="POST" autocomplete="off">
        <input type="text" name="mensaje" placeholder="Escribe tu mensaje..." required>
        <button type="submit">Enviar</button>
      </form>
    </div>
  </div>

  <script>
    // Scroll automático al final (scrollTop)
    (function(){
      const chat = document.getElementById('chat');
      if (!chat) return;
      chat.scrollTop = chat.scrollHeight;
    })();
  </script>
</body>
</html>
