<?php
// chat.php — single-file ChatGPT-like UI (HTML+CSS+PHP)
// Uses a Python script inside a venv (so torch exists).
//
// Folder (your path):
// /var/www/html/programaciondam2526/012-Inteligencia Artificial/009-Entrenamiento dia 2/101-Ejercicios
//
// Run (CLI dev server):
//   cd "/var/www/html/programaciondam2526/012-Inteligencia Artificial/009-Entrenamiento dia 2/101-Ejercicios"
//   php -S localhost:8000
//   open http://localhost:8000/chat.php
//
// IMPORTANT:
// - Put this file in the same folder as your python infer script.
// - Ensure your venv is in: ./venv/ (or edit $VENV_PY below).
// - Ensure your python infer script is named: 003-inferir.py (or edit $PY_SCRIPT below).

declare(strict_types=1);
session_start();

// ---------------------------------------------------------------------
// CONFIG (adjust only if your filenames differ)
// ---------------------------------------------------------------------
$BASE_DIR   = __DIR__;
$VENV_PY    = $BASE_DIR . '/venv/bin/python3';     // venv python (NO "activate" needed)
$PY_SCRIPT  = $BASE_DIR . '/003-inferir.py';       // your infer script
$MAX_TURNS  = 24;

// Avoid Ubuntu apport crash reporting attempts writing to /var/crash (permission issue under www-data)
putenv('APPORT_DISABLE=1');
putenv('PYTHONNOUSERSITE=1');

// Optional: ensure HF cache is writable next to this PHP (same idea as in your infer script)
$HF_CACHE = $BASE_DIR . '/.hf-cache';
if (!is_dir($HF_CACHE)) @mkdir($HF_CACHE, 0775, true);
putenv('HF_HOME=' . $HF_CACHE);

// ---------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------
function h(string $s): string {
  return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function add_msg(string $role, string $content): void {
  $_SESSION['chat'][] = ['role' => $role, 'content' => $content];
}

function clamp_history(int $max): void {
  if (count($_SESSION['chat']) > $max) {
    $_SESSION['chat'] = array_slice($_SESSION['chat'], -$max);
  }
}

function run_python(string $py, string $script, string $prompt): array {
  // Returns [ok(bool), out(string)]
  if (!is_file($py)) {
    return [false, "No encuentro el Python del venv en:\n$py\n\nCrea el venv en ./venv o ajusta \$VENV_PY."];
  }
  if (!is_executable($py)) {
    return [false, "El Python del venv no es ejecutable:\n$py\n\nPrueba: chmod +x \"$py\""];
  }
  if (!is_file($script)) {
    return [false, "No encuentro el script de inferencia en:\n$script\n\nAsegúrate de que exista (p. ej. 003-inferir.py)."];
  }

  // Use direct venv python to avoid "import torch" missing.
  $cmd = escapeshellarg($py) . ' ' . escapeshellarg($script) . ' ' . escapeshellarg($prompt) . ' 2>&1';
  $out = shell_exec($cmd);

  if ($out === null) {
    return [false, "shell_exec devolvió NULL. Posibles causas:\n- shell_exec deshabilitado en php.ini\n- permisos insuficientes\n- error al lanzar el proceso"];
  }
  $out = trim((string)$out);
  return [true, $out === '' ? '(sin salida)' : $out];
}

// ---------------------------------------------------------------------
// Init conversation
// ---------------------------------------------------------------------
if (!isset($_SESSION['chat']) || !is_array($_SESSION['chat'])) {
  $_SESSION['chat'] = [
    ['role' => 'assistant', 'content' => 'Hola. ¿En qué puedo ayudarte?'],
  ];
}

// ---------------------------------------------------------------------
// Actions
// ---------------------------------------------------------------------
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $action = (string)($_POST['action'] ?? '');

  if ($action === 'reset') {
    $_SESSION['chat'] = [
      ['role' => 'assistant', 'content' => 'Conversación reiniciada. ¿Qué quieres preguntar?'],
    ];
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit;
  }

  if ($action === 'send') {
    $msg = (string)($_POST['message'] ?? '');
    $msg = trim(str_replace("\0", "", $msg));

    if ($msg !== '') {
      add_msg('user', $msg);

      // Build compact context for the model (last 10 messages)
      $tail = array_slice($_SESSION['chat'], -10);
      $ctx = [];
      foreach ($tail as $m) {
        $r = ($m['role'] === 'user') ? 'USER' : 'ASSISTANT';
        $ctx[] = $r . ': ' . $m['content'];
      }

      $prompt_for_model =
        "Responde en español de forma clara.\n" .
        "Si no conoces la respuesta, indícalo.\n\n" .
        implode("\n", $ctx) . "\nASSISTANT:";

      [$ok, $out] = run_python($VENV_PY, $PY_SCRIPT, $prompt_for_model);

      if (!$ok) {
        add_msg('assistant', "⚠️ Error ejecutando el modelo:\n\n" . $out);
      } else {
        add_msg('assistant', $out);
      }

      clamp_history($MAX_TURNS);
    }

    header('Location: ' . $_SERVER['PHP_SELF']);
    exit;
  }
}

// ---------------------------------------------------------------------
// UI
// ---------------------------------------------------------------------
?><!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Chat (local)</title>
  <style>
    :root{
      --bg:#0b0f19;
      --panel:#0f172a;
      --panel2:#0b1222;
      --text:#e5e7eb;
      --muted:#9ca3af;
      --border:rgba(255,255,255,.09);
      --accent:#22c55e;
      --shadow: 0 14px 36px rgba(0,0,0,.42);
      --radius: 14px;
      --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      --sans: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
    }
    *{box-sizing:border-box}
    body{
      margin:0;
      font-family:var(--sans);
      background:
        radial-gradient(1100px 700px at 25% 10%, rgba(34,197,94,.14), transparent 60%),
        radial-gradient(900px 600px at 85% 22%, rgba(59,130,246,.10), transparent 55%),
        var(--bg);
      color:var(--text);
      height:100vh;
      display:flex;
      justify-content:center;
      align-items:stretch;
    }
    .app{
      width:min(1000px, 100%);
      padding:18px;
      display:flex;
      flex-direction:column;
      gap:12px;
    }
    header{
      display:flex;
      align-items:center;
      justify-content:space-between;
      gap:10px;
      padding:12px 14px;
      background:linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,.02));
      border:1px solid var(--border);
      border-radius:var(--radius);
      box-shadow:var(--shadow);
    }
    .brand{display:flex; align-items:center; gap:10px; min-width:0;}
    .dot{
      width:10px;height:10px;border-radius:999px;
      background:var(--accent);
      box-shadow:0 0 0 6px rgba(34,197,94,.12);
      flex:0 0 auto;
    }
    .title{font-weight:750; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;}
    .sub{font-size:12px; color:var(--muted); margin-top:2px;}
    .right{display:flex; gap:8px; align-items:center; flex:0 0 auto;}
    .btn{
      border:1px solid var(--border);
      background:rgba(255,255,255,.04);
      color:var(--text);
      padding:8px 10px;
      border-radius:12px;
      cursor:pointer;
      font-size:13px;
    }
    .btn:hover{background:rgba(255,255,255,.07)}
    .chat{
      flex:1 1 auto;
      overflow:auto;
      padding:14px;
      background:rgba(15,23,42,.55);
      border:1px solid var(--border);
      border-radius:var(--radius);
      box-shadow:var(--shadow);
    }
    .msg{
      display:flex;
      gap:10px;
      margin:10px 0;
      align-items:flex-start;
    }
    .avatar{
      width:34px;height:34px;border-radius:12px;
      background:rgba(255,255,255,.06);
      border:1px solid var(--border);
      display:flex;align-items:center;justify-content:center;
      font-family:var(--mono);
      color:var(--muted);
      flex:0 0 auto;
      user-select:none;
    }
    .bubble{
      max-width: 820px;
      padding:12px 14px;
      border-radius:14px;
      border:1px solid var(--border);
      background:rgba(255,255,255,.03);
      line-height:1.45;
      white-space:pre-wrap;
      word-break:break-word;
    }
    .user .bubble{ background: rgba(31,41,55,.55); }
    .assistant .bubble{ background: rgba(11,18,34,.70); }
    .meta{font-size:12px; color:var(--muted); margin-top:6px;}
    .composer{
      display:flex;
      gap:10px;
      padding:12px;
      background:linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,.02));
      border:1px solid var(--border);
      border-radius:var(--radius);
      box-shadow:var(--shadow);
    }
    textarea{
      flex:1 1 auto;
      resize:none;
      border:1px solid var(--border);
      background:rgba(255,255,255,.03);
      color:var(--text);
      padding:10px 12px;
      border-radius:12px;
      outline:none;
      min-height:48px;
      max-height:180px;
      font-family:var(--sans);
      font-size:14px;
      line-height:1.35;
    }
    textarea:focus{
      border-color: rgba(34,197,94,.35);
      box-shadow:0 0 0 6px rgba(34,197,94,.08);
    }
    .send{
      border:none;
      background: linear-gradient(180deg, rgba(34,197,94,.95), rgba(34,197,94,.75));
      color:#05210f;
      padding:0 14px;
      border-radius:12px;
      cursor:pointer;
      font-weight:750;
      min-width:92px;
    }
    .send:hover{filter:brightness(1.05)}
    .hint{
      font-size:12px;
      color:var(--muted);
      padding:0 6px 6px 6px;
    }
    code, pre{font-family:var(--mono); font-size:13px;}
  </style>
</head>
<body>
  <div class="app">
    <header>
      <div class="brand">
        <div class="dot"></div>
        <div style="min-width:0">
          <div class="title">Chat local (PHP ↔ venv ↔ modelo)</div>
          <div class="sub"><?= h($BASE_DIR) ?></div>
        </div>
      </div>
      <div class="right">
        <form method="post" style="margin:0">
          <input type="hidden" name="action" value="reset">
          <button class="btn" type="submit">Reiniciar</button>
        </form>
      </div>
    </header>

    <div class="chat" id="chat">
      <?php foreach ($_SESSION['chat'] as $m): $isUser = ($m['role'] === 'user'); ?>
        <div class="msg <?= $isUser ? 'user' : 'assistant' ?>">
          <div class="avatar"><?= $isUser ? 'U' : 'AI' ?></div>
          <div>
            <div class="bubble"><?= h((string)$m['content']) ?></div>
            <div class="meta"><?= $isUser ? 'Tú' : 'Asistente' ?></div>
          </div>
        </div>
      <?php endforeach; ?>
    </div>

    <div class="hint">
      Usa <code>Ctrl+Enter</code> para enviar. Ejecuta Python desde venv:
      <code><?= h($VENV_PY) ?></code> · Script: <code><?= h($PY_SCRIPT) ?></code>
    </div>

    <form class="composer" method="post" autocomplete="off">
      <input type="hidden" name="action" value="send">
      <textarea name="message" id="message" placeholder="Escribe tu mensaje..." required></textarea>
      <button class="send" type="submit">Enviar</button>
    </form>
  </div>

  <script>
    // Auto-scroll
    const chat = document.getElementById('chat');
    chat.scrollTop = chat.scrollHeight;

    // Ctrl+Enter to send
    const ta = document.getElementById('message');
    ta.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        ta.form.submit();
      }
    });

    // Auto-grow textarea
    const grow = () => {
      ta.style.height = 'auto';
      ta.style.height = Math.min(180, ta.scrollHeight) + 'px';
    };
    ta.addEventListener('input', grow);
    grow();
  </script>
</body>
</html>
