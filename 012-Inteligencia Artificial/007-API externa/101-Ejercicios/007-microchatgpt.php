<?php
declare(strict_types=1);
session_start();

/*
  microchat.php — Single-file HTML+CSS+PHP "micro-ChatGPT"

  Requisitos:
  - PHP 8.1+
  - cURL habilitado
  - Variable de entorno OPENAIAPI con tu API key:
      export OPENAIAPI="sk-..."
*/

$API_KEY = getenv('OPENAIAPI') ?: '';
$MODEL   = 'gpt-4.1-mini';

if (!isset($_SESSION['chat'])) {
  $_SESSION['chat'] = [
    ['role' => 'system', 'content' => 'You are a helpful assistant.']
  ];
}

function h(string $s): string {
  return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function openai_chat(array $messages, string $apiKey, string $model, float $temperature = 0.3): array {
  $url = 'https://api.openai.com/v1/chat/completions';

  $payload = [
    'model' => $model,
    'messages' => $messages,
    'temperature' => $temperature,
  ];

  $ch = curl_init($url);
  curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
      'Content-Type: application/json',
      'Authorization: Bearer ' . $apiKey,
    ],
    CURLOPT_POSTFIELDS => json_encode($payload, JSON_UNESCAPED_UNICODE),
    CURLOPT_TIMEOUT => 60,
  ]);

  $raw = curl_exec($ch);
  $errno = curl_errno($ch);
  $err = curl_error($ch);
  $http = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);

  if ($errno) {
    return ['ok' => false, 'error' => "cURL error ($errno): $err"];
  }

  $data = json_decode((string)$raw, true);
  if (!is_array($data)) {
    return ['ok' => false, 'error' => 'Respuesta no válida (JSON).', 'raw' => $raw, 'http' => $http];
  }

  if ($http < 200 || $http >= 300) {
    $msg = $data['error']['message'] ?? ('HTTP ' . $http);
    return ['ok' => false, 'error' => $msg, 'http' => $http, 'data' => $data];
  }

  $content = $data['choices'][0]['message']['content'] ?? '';
  return ['ok' => true, 'content' => $content, 'data' => $data];
}

$action = $_POST['action'] ?? '';
$error = null;

if ($action === 'reset') {
  $_SESSION['chat'] = [
    ['role' => 'system', 'content' => 'You are a helpful assistant.']
  ];
  header('Location: ' . strtok($_SERVER['REQUEST_URI'], '?'));
  exit;
}

if ($action === 'send') {
  $userMsg = trim((string)($_POST['message'] ?? ''));

  if ($userMsg === '') {
    $error = 'Escribe un mensaje.';
  } elseif ($API_KEY === '') {
    $error = 'Falta la API key: define la variable de entorno OPENAIAPI.';
  } else {
    // Añade mensaje del usuario
    $_SESSION['chat'][] = ['role' => 'user', 'content' => $userMsg];

    // Llamada a OpenAI
    $result = openai_chat($_SESSION['chat'], $API_KEY, $MODEL, 0.3);

    if (!$result['ok']) {
      $error = 'Error de OpenAI: ' . ($result['error'] ?? 'desconocido');
      // En caso de error, opcionalmente revertir el último mensaje del usuario:
      // array_pop($_SESSION['chat']);
    } else {
      $_SESSION['chat'][] = ['role' => 'assistant', 'content' => (string)$result['content']];
    }

    // Limitar historial para no crecer sin control (mantiene system + últimas 20 intervenciones)
    $system = $_SESSION['chat'][0];
    $rest = array_slice($_SESSION['chat'], 1);
    if (count($rest) > 40) $rest = array_slice($rest, -40);
    $_SESSION['chat'] = array_merge([$system], $rest);

    // PRG pattern
    header('Location: ' . strtok($_SERVER['REQUEST_URI'], '?'));
    exit;
  }
}

$chat = $_SESSION['chat'];
?>
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Micro-ChatGPT (PHP)</title>
  <style>
    :root{
      --bg:#0b0f14;
      --panel:#0f1621;
      --panel2:#0d131c;
      --text:#e6edf3;
      --muted:#9fb0c0;
      --line: rgba(255,255,255,.10);
      --accent:#4aa3ff;
      --accent2:#71d39b;
      --danger:#ff5d5d;
      --shadow: 0 10px 30px rgba(0,0,0,.35);
      --radius: 18px;
      --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      --sans: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, "Noto Sans", Arial, "Apple Color Emoji","Segoe UI Emoji";
    }
    *{ box-sizing:border-box; }
    body{
      margin:0;
      background: radial-gradient(1200px 700px at 20% -10%, rgba(74,163,255,.25), transparent 55%),
                  radial-gradient(900px 600px at 110% 10%, rgba(113,211,155,.22), transparent 50%),
                  var(--bg);
      color:var(--text);
      font-family:var(--sans);
      min-height:100vh;
      display:flex;
      align-items:center;
      justify-content:center;
      padding:22px;
    }
    .app{
      width:min(980px, 100%);
      background: linear-gradient(180deg, rgba(255,255,255,.04), transparent 180px), var(--panel);
      border:1px solid var(--line);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      overflow:hidden;
    }
    header{
      display:flex;
      gap:14px;
      align-items:center;
      justify-content:space-between;
      padding:16px 18px;
      background: linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,0));
      border-bottom:1px solid var(--line);
    }
    .title{
      display:flex;
      flex-direction:column;
      gap:2px;
    }
    .title h1{
      margin:0;
      font-size:16px;
      letter-spacing:.2px;
      font-weight:650;
    }
    .title .sub{
      font-size:12px;
      color:var(--muted);
      font-family:var(--mono);
    }
    .actions{
      display:flex;
      gap:10px;
      align-items:center;
    }
    button, .btn{
      appearance:none;
      border:1px solid var(--line);
      background: rgba(255,255,255,.04);
      color:var(--text);
      padding:10px 12px;
      border-radius:14px;
      cursor:pointer;
      font-weight:600;
      font-size:13px;
      transition: transform .06s ease, background .15s ease, border-color .15s ease;
      user-select:none;
    }
    button:hover, .btn:hover{
      background: rgba(255,255,255,.07);
      border-color: rgba(255,255,255,.18);
    }
    button:active, .btn:active{ transform: translateY(1px); }
    .btn-danger{
      border-color: rgba(255,93,93,.35);
      background: rgba(255,93,93,.08);
    }
    .btn-danger:hover{
      background: rgba(255,93,93,.12);
      border-color: rgba(255,93,93,.55);
    }
    .wrap{
      display:grid;
      grid-template-columns: 1fr;
      gap:0;
    }
    .chat{
      height: min(66vh, 620px);
      overflow:auto;
      padding:18px;
      background: linear-gradient(180deg, rgba(0,0,0,.15), rgba(0,0,0,.0)), var(--panel2);
    }
    .msg{
      display:flex;
      gap:12px;
      margin: 0 0 14px 0;
      align-items:flex-start;
    }
    .avatar{
      width:32px;height:32px;
      border-radius:12px;
      display:grid;
      place-items:center;
      font-weight:800;
      font-family:var(--mono);
      font-size:13px;
      border:1px solid var(--line);
      background: rgba(255,255,255,.05);
      flex: 0 0 auto;
    }
    .avatar.user{ background: rgba(74,163,255,.10); border-color: rgba(74,163,255,.25); }
    .avatar.asst{ background: rgba(113,211,155,.10); border-color: rgba(113,211,155,.25); }
    .bubble{
      max-width: 78ch;
      width: fit-content;
      padding: 12px 14px;
      border-radius: 16px;
      border:1px solid var(--line);
      background: rgba(255,255,255,.04);
      line-height:1.45;
      white-space:pre-wrap;
      word-wrap:break-word;
    }
    .bubble.user{
      border-color: rgba(74,163,255,.25);
      background: rgba(74,163,255,.07);
    }
    .bubble.asst{
      border-color: rgba(113,211,155,.25);
      background: rgba(113,211,155,.07);
    }
    .meta{
      margin-top:6px;
      font-size:11px;
      color: var(--muted);
      font-family: var(--mono);
    }
    .composer{
      padding:14px;
      border-top:1px solid var(--line);
      background: rgba(255,255,255,.03);
    }
    form.send{
      display:flex;
      gap:10px;
      align-items:flex-end;
    }
    textarea{
      width:100%;
      min-height: 52px;
      max-height: 160px;
      resize: vertical;
      padding: 12px 12px;
      border-radius: 16px;
      border:1px solid var(--line);
      background: rgba(0,0,0,.25);
      color: var(--text);
      outline:none;
      line-height:1.35;
      font-size:14px;
    }
    textarea:focus{
      border-color: rgba(74,163,255,.45);
      box-shadow: 0 0 0 4px rgba(74,163,255,.12);
    }
    .sendbtn{
      background: linear-gradient(180deg, rgba(74,163,255,.25), rgba(74,163,255,.10));
      border-color: rgba(74,163,255,.45);
      padding: 12px 14px;
      border-radius: 16px;
    }
    .hint{
      display:flex;
      justify-content:space-between;
      gap:12px;
      margin-top:10px;
      color: var(--muted);
      font-size:12px;
      font-family: var(--mono);
    }
    .error{
      margin: 12px 18px 0 18px;
      padding: 10px 12px;
      border-radius: 14px;
      border:1px solid rgba(255,93,93,.40);
      background: rgba(255,93,93,.10);
      color: #ffd7d7;
      font-family: var(--mono);
      font-size: 12px;
    }
    .kbd{
      border:1px solid var(--line);
      border-bottom-color: rgba(255,255,255,.06);
      background: rgba(255,255,255,.04);
      padding: 2px 6px;
      border-radius: 8px;
      font-size: 11px;
      color: var(--text);
    }
  </style>
</head>
<body>
  <div class="app">
    <header>
      <div class="title">
        <h1>Micro-ChatGPT (PHP)</h1>
        <div class="sub">model: <?=h($MODEL)?> · env: OPENAIAPI <?= $API_KEY !== '' ? '✓' : '✗' ?></div>
      </div>
      <div class="actions">
        <form method="post" style="margin:0">
          <input type="hidden" name="action" value="reset">
          <button class="btn btn-danger" type="submit" title="Borrar conversación">Reset</button>
        </form>
      </div>
    </header>

    <?php if ($error): ?>
      <div class="error"><?=h($error)?></div>
    <?php endif; ?>

    <div class="wrap">
      <div class="chat" id="chat">
        <?php
          // Renderiza chat (oculta system)
          foreach ($chat as $i => $m) {
            if (($m['role'] ?? '') === 'system') continue;
            $role = (string)($m['role'] ?? 'assistant');
            $content = (string)($m['content'] ?? '');
            $isUser = $role === 'user';
            $av = $isUser ? 'U' : 'A';
            $cls = $isUser ? 'user' : 'asst';
            echo '<div class="msg">';
            echo '  <div class="avatar ' . $cls . '">' . $av . '</div>';
            echo '  <div>';
            echo '    <div class="bubble ' . $cls . '">' . h($content) . '</div>';
            echo '    <div class="meta">' . h($role) . '</div>';
            echo '  </div>';
            echo '</div>';
          }

          if (count($chat) <= 1) {
            echo '<div class="msg">';
            echo '  <div class="avatar asst">A</div>';
            echo '  <div>';
            echo '    <div class="bubble asst">Escribe un mensaje para empezar. Ejemplo: "Haz un resumen de la situación geopolítica mundial."</div>';
            echo '    <div class="meta">assistant</div>';
            echo '  </div>';
            echo '</div>';
          }
        ?>
      </div>

      <div class="composer">
        <form class="send" method="post" id="sendForm">
          <input type="hidden" name="action" value="send">
          <textarea
            name="message"
            id="message"
            placeholder="Escribe aquí…"
            required
          ></textarea>
          <button class="sendbtn" type="submit">Enviar</button>
        </form>
        <div class="hint">
          <div>Atajo: <span class="kbd">Ctrl</span> + <span class="kbd">Enter</span> para enviar</div>
          <div>Historial: sesión (server-side)</div>
        </div>
      </div>
    </div>
  </div>

  <script>
    // Scroll al final
    const chat = document.getElementById('chat');
    chat.scrollTop = chat.scrollHeight;

    // Ctrl+Enter para enviar
    const ta = document.getElementById('message');
    const form = document.getElementById('sendForm');
    ta.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        form.submit();
      }
    });
  </script>
</body>
</html>
