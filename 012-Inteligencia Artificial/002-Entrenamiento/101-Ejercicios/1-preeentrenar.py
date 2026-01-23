#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generador de pares Q/A en formato JSONL a partir de HTML, PDF, texto plano o Markdown.

- Recorre recursivamente todos los ficheros de INPUT_DIR con extensión:
    .html, .htm, .pdf, .txt, .md
- Para HTML:
    * Lee el archivo.
    * Limpia el markup (quita <script>, <style>, etc.).
    * Extrae el texto relevante.
- Para PDF:
    * Extrae el texto con PyPDF2.
- Para .txt / .md:
    * Igual que antes: limpia Markdown si procede.
- Trocea cada texto en bloques con solape.
- Para cada bloque lanza VARIAS rondas de prompts a Ollama:
    * Rondas de preguntas fáciles / introductorias.
    * Rondas de preguntas intermedias / avanzadas.
- En cada ronda se pide que genere AL MENOS ~30 pares Q/A si el texto lo permite.
- Genera UN JSONL POR ARCHIVO de entrada en OUTPUT_DIR.
- Mantiene un log.json con la lista de ficheros ya procesados para no duplicar materiales.

Características extra:
- Comprueba al inicio si Ollama está accesible.
- Detecta automáticamente si debe usar /api/chat o /api/generate.
- Guarda las Q/A sobre la marcha (bloque a bloque) en el JSONL, sin esperar al final.
- Muestra una barra de progreso global con:
    * porcentaje completado,
    * tiempo transcurrido,
    * tiempo estimado restante (ETA).

Esta versión está afinada para maximizar la cantidad de pares Q/A generados,
aunque aumente considerablemente el tiempo de ejecución.

Extensión adicional:
- Al finalizar la ejecución principal, genera un informe Markdown en OUTPUT_DIR
  con trazabilidad completa de la ejecución y listado de todos los pares Q/A
  generados en esta ejecución.
"""

import os
import re
import json
import time
import shutil
import requests
import platform
from datetime import datetime
from typing import List, Dict, Optional, Tuple

from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

# =========================
# CONFIGURACIÓN GENERAL
# =========================

# Carpeta de entrada: aquí pondrás tu 'paginas_html'
INPUT_DIR = "paginas_html"

# Carpeta de salida (JSONL + reportes)
OUTPUT_DIR = "outputs"
LOG_FILE = os.path.join(OUTPUT_DIR, "log.json")

# Ollama
OLLAMA_BASE_URL = "http://localhost:11434"
# Ajusta aquí el modelo que vayas a usar
MODEL_NAME = "llama3.2:latest"

# Estos se rellenarán en detect_ollama_mode()
OLLAMA_MODE: Optional[str] = None   # "chat" o "generate"
OLLAMA_URL: Optional[str] = None    # URL completa del endpoint elegido

# Troceado del texto: bloques algo más pequeños con más solape
MAX_CHARS_PER_BLOCK = 2800  # tamaño objetivo de cada bloque
BLOCK_OVERLAP = 700         # solape entre bloques para no perder contexto

# Generación de Q/A
# Temperatura algo mayor para favorecer variedad de preguntas,
# pero sin irnos a valores demasiado caóticos.
TEMPERATURE = 0.45
# Límite aproximado de tokens generados por respuesta de Ollama
# (subido para permitir MUCHAS preguntas por llamada)
MAX_TOKENS = 1536

# Rondas por bloque: más rondas = muchas más Q/A
ROUNDS_EASY = 2        # número de rondas de preguntas fáciles por bloque
ROUNDS_ADVANCED = 3    # número de rondas de preguntas avanzadas por bloque

# Extensiones aceptadas
VALID_EXTS = (".html", ".htm", ".pdf", ".txt", ".md")


# =========================
# UTILIDADES BÁSICAS
# =========================

def ensure_dirs():
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def normalize_whitespace(text: str) -> str:
    # Quita espacios duplicados, saltos de línea raros, etc.
    return " ".join(text.split())


def strip_markdown(text: str) -> str:
    """
    Elimina en lo posible el "ruido" de Markdown para dejar solo texto útil.
    """

    # Bloques de código triple
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    # Código en línea `code`
    text = re.sub(r"`([^`]*)`", r"\1", text)

    # Imágenes ![alt](url)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)

    # Enlaces [texto](url) -> texto
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)

    # Cabeceras tipo #, ##, ### al inicio de línea
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)

    # Marcadores de lista al inicio de línea: -, *, +
    text = re.sub(r"^[\-\*\+]\s+", "", text, flags=re.MULTILINE)

    # Negritas/cursivas: **texto**, *texto*, __texto__, _texto_
    text = text.replace("**", "").replace("__", "")
    text = text.replace("*", "").replace("_", "")

    return text


def split_into_blocks(text: str,
                      max_chars: int = MAX_CHARS_PER_BLOCK,
                      overlap: int = BLOCK_OVERLAP) -> List[str]:
    """
    Trocea el texto en bloques de tamaño aproximado `max_chars`,
    con un solape de `overlap` caracteres entre bloques consecutivos.
    """
    text = text.strip()
    if len(text) <= max_chars:
        return [text] if text else []

    blocks = []
    start = 0
    n = len(text)

    while start < n:
        end = min(start + max_chars, n)

        # Intentar cortar cerca de un final de frase (., ?, !)
        split_pos = end
        for sep in [".", "?", "!", "¿", "¡"]:
            pos = text.rfind(sep, start + int(max_chars * 0.6), end)
            if pos != -1 and pos > start:
                split_pos = max(split_pos, pos + 1)

        if split_pos == end:  # no encontró nada razonable
            split_pos = end

        block = text[start:split_pos].strip()
        if block:
            blocks.append(block)

        if split_pos >= n:
            break

        # Retrocede un poco para crear solape
        start = max(0, split_pos - overlap)

    return blocks


# =========================
# EXTRACCIÓN DESDE HTML Y PDF
# =========================

def extract_text_from_html(path: str) -> str:
    """
    Extrae texto "importante" de un HTML:
    - Elimina <script>, <style>, <noscript>.
    - Se queda con encabezados, párrafos, listas, etc.
    - Devuelve el texto plano concatenado.
    """
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()
    except Exception as e:
        print(f"[WARN] No se pudo leer HTML {path}: {e}")
        return ""

    soup = BeautifulSoup(html, "html.parser")

    # Eliminar ruido
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # También puedes eliminar nav/footer si quieres:
    for tag in soup(["nav", "footer"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)
    return text


def extract_text_from_pdf(path: str) -> str:
    """
    Extrae texto de un PDF usando PyPDF2.
    """
    try:
        reader = PdfReader(path)
    except Exception as e:
        print(f"[WARN] No se pudo abrir PDF {path}: {e}")
        return ""

    pages_text = []
    for i, page in enumerate(reader.pages):
        try:
            t = page.extract_text()
        except Exception as e:
            print(f"[WARN] Error extrayendo texto de la página {i} en {path}: {e}")
            t = None
        if t:
            pages_text.append(t)

    return "\n".join(pages_text)


# =========================
# GESTIÓN DEL LOG
# =========================

def load_log() -> Dict:
    """
    Carga el log de ficheros procesados.

    Estructura:
    {
        "processed_files": [
            "paginas_html/index.html",
            "paginas_html/wp-content/...",
            ...
        ]
    }
    """
    if not os.path.exists(LOG_FILE):
        return {"processed_files": []}

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if "processed_files" not in data or not isinstance(data["processed_files"], list):
            return {"processed_files": []}
        return data
    except Exception:
        # Si el log está corrupto, empezamos de cero para no bloquear el proceso.
        return {"processed_files": []}


def save_log(log: Dict):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)


# =========================
# TRACKER DE PROGRESO
# =========================

class ProgressTracker:
    """
    Barra de progreso global basada en número total de bloques.
    Muestra:
    - porcentaje completado
    - tiempo transcurrido
    - ETA estimada
    """

    def __init__(self, total_units: int):
        self.total = max(1, total_units)
        self.current = 0
        self.start_time = time.time()

    @staticmethod
    def _format_seconds(secs: float) -> str:
        secs = int(secs)
        h = secs // 3600
        m = (secs % 3600) // 60
        s = secs % 60
        if h > 0:
            return f"{h:02d}:{m:02d}:{s:02d}"
        return f"{m:02d}:{s:02d}"

    def update(self, step: int = 1, prefix: str = ""):
        self.current += step
        if self.current > self.total:
            self.current = self.total

        elapsed = time.time() - self.start_time
        percent = (self.current / self.total) * 100.0

        if self.current > 0:
            rate = elapsed / self.current
            remaining = rate * (self.total - self.current)
        else:
            remaining = 0.0

        try:
            term_width = shutil.get_terminal_size((80, 20)).columns
        except Exception:
            term_width = 80

        bar_len = max(10, term_width - 55)
        filled = int(bar_len * self.current / self.total)
        bar = "█" * filled + "░" * (bar_len - filled)

        msg = (
            f"{prefix} [{bar}] {percent:6.2f}% "
            f"| t+{self._format_seconds(elapsed)} "
            f"| ETA {self._format_seconds(remaining)}"
        )

        msg = msg[:term_width - 1]
        print("\r" + msg, end="", flush=True)

    def finish(self, prefix: str = ""):
        self.update(step=0, prefix=prefix)
        print()  # salto de línea final


# =========================
# DETECCIÓN DEL MODO OLLAMA
# =========================

def detect_ollama_mode() -> bool:
    """
    Detecta si Ollama expone /api/chat o /api/generate y configura
    las variables globales OLLAMA_MODE y OLLAMA_URL.
    """
    global OLLAMA_MODE, OLLAMA_URL

    # Primero probamos /api/chat
    chat_url = f"{OLLAMA_BASE_URL}/api/chat"
    print(f"[INFO] Probando endpoint: {chat_url}")
    try:
        payload_chat = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": "Responde con una sola palabra: OK"},
                {"role": "user", "content": "OK"}
            ],
            "stream": False
        }
        resp = requests.post(chat_url, json=payload_chat, timeout=10)

        if resp.status_code == 404:
            print("[INFO] /api/chat devuelve 404, se probará /api/generate.")
        else:
            resp.raise_for_status()
            data = resp.json()
            if "message" in data and "content" in data["message"]:
                print("[INFO] Endpoint /api/chat detectado correctamente.")
                OLLAMA_MODE = "chat"
                OLLAMA_URL = chat_url
                return True
            else:
                print("[WARN] /api/chat respondió pero no con el formato esperado.")
    except requests.exceptions.ConnectionError:
        print(f"[ERROR] No se puede conectar a Ollama en {OLLAMA_BASE_URL}")
        print("       ¿Está arrancado? Ejecuta:  ollama serve")
        return False
    except Exception as e:
        print(f"[WARN] Error al probar /api/chat: {e}")

    # Si /api/chat no sirve, probamos /api/generate
    gen_url = f"{OLLAMA_BASE_URL}/api/generate"
    print(f"[INFO] Probando endpoint: {gen_url}")
    try:
        payload_gen = {
            "model": MODEL_NAME,
            "prompt": "Responde con una sola palabra: OK",
            "stream": False
        }
        resp = requests.post(gen_url, json=payload_gen, timeout=10)

        if resp.status_code == 404:
            print("[ERROR] /api/generate también devuelve 404.")
            print("[ERROR] Ninguno de los endpoints estándar de Ollama está disponible.")
            print("[ERROR] Revisa el nombre del modelo o si Ollama está arrancado.")
            print("       Modelo actual:", MODEL_NAME)
            return False

        resp.raise_for_status()
        data = resp.json()
        if "response" in data:
            print("[INFO] Endpoint /api/generate detectado correctamente.")
            OLLAMA_MODE = "generate"
            OLLAMA_URL = gen_url
            return True
        else:
            print("[WARN] /api/generate respondió pero no con el formato esperado.")
            return False

    except requests.exceptions.ConnectionError:
        print(f"[ERROR] No se puede conectar a Ollama en {OLLAMA_BASE_URL}")
        print("       ¿Está arrancado? Ejecuta:  ollama serve")
        return False
    except Exception as e:
        print(f"[ERROR] Error al probar /api/generate: {e}")
        return False


# =========================
# LLAMADA A OLLAMA (según modo detectado)
# =========================

def call_ollama(system_prompt: str, user_prompt: str) -> str:
    """
    Llama a Ollama usando el endpoint detectado (chat o generate).
    """
    if OLLAMA_MODE is None or OLLAMA_URL is None:
        raise RuntimeError("OLLAMA_MODE no está configurado. Llama antes a detect_ollama_mode().")

    if OLLAMA_MODE == "chat":
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "stream": False,
            "options": {
                "temperature": TEMPERATURE,
                "num_predict": MAX_TOKENS
            }
        }
    elif OLLAMA_MODE == "generate":
        full_prompt = f"""{system_prompt.strip()}

Usuario:
{user_prompt.strip()}
"""
        payload = {
            "model": MODEL_NAME,
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "temperature": TEMPERATURE,
                "num_predict": MAX_TOKENS
            }
        }
    else:
        raise RuntimeError(f"Modo de Ollama desconocido: {OLLAMA_MODE}")

    resp = requests.post(OLLAMA_URL, json=payload, timeout=300)
    resp.raise_for_status()
    data = resp.json()

    if OLLAMA_MODE == "chat":
        return data["message"]["content"]
    else:  # generate
        return data.get("response", "")


# =========================
# PROMPTS PARA Q/A
# =========================

SYSTEM_PROMPT_QA = """
Eres un generador de preguntas y respuestas de alta calidad en español
para entrenar un modelo de lenguaje educativo.

Tu tarea:
- Leer con mucha atención un bloque de texto técnico o formativo en español
  (puede venir originalmente de HTML o PDF).
- Identificar TODOS los conceptos importantes posibles (términos, pasos, advertencias,
  decisiones de diseño, buenas prácticas, errores habituales, matices, ejemplos, etc.).
- A partir de esos conceptos, generar el máximo número posible de preguntas y respuestas
  útiles para entrenamiento, sin omitir detalles relevantes.

Reglas generales:
- No inventes conceptos que no aparezcan o no se deduzcan claramente del texto.
- Las respuestas deben ser completas pero concisas, sin relleno.
- Siempre responde en español neutro.
- Intenta formular varias preguntas diferentes sobre un mismo concepto
  (definición, uso, matices, errores típicos, etc.) si el texto lo permite.
- Usa el formato JSON Lines: cada línea un objeto JSON con campos:
  {"question": "...", "answer": "..."}
- No añadas texto fuera de ese formato (ni comentarios, ni encabezados).
- No pongas comas finales después del objeto JSON en cada línea.
""".strip()


def build_user_prompt_easy(block: str, round_index: int = 1) -> str:
    return f"""
Genera PREGUNTAS FÁCILES (nivel introductorio) con sus respuestas a partir del siguiente texto.

Requisitos:
- Preguntas de tipo:
  * definición (¿qué es...?),
  * propósito (¿para qué sirve...?),
  * pasos básicos (¿cuál es el primer paso para...?),
  * identificación (¿qué nombre recibe...?),
  * ventajas / desventajas claras.
- Cubre todos los conceptos básicos que veas.
- FORMULA VARIAS PREGUNTAS DISTINTAS SOBRE EL MISMO CONCEPTO si es posible.
- COMO NORMA GENERAL, genera AL MENOS 30 pares pregunta-respuesta para este bloque,
  y más si el texto lo permite.
- Esta es la ronda {round_index} de generación para este mismo bloque de texto.
  NO repitas literalmente preguntas que ya habrías generado en rondas anteriores;
  busca nuevos enfoques y matices.
- Formato OBLIGATORIO: JSON Lines, cada línea:
  {{"question": "texto de la pregunta", "answer": "texto de la respuesta"}}

Texto:
\"\"\"{block}\"\"\"
""".strip()


def build_user_prompt_advanced(block: str, round_index: int = 1) -> str:
    return f"""
Genera PREGUNTAS INTERMEDIAS y AVANZADAS con sus respuestas a partir del siguiente texto.

Requisitos:
- Preguntas de tipo:
  * razonamiento (¿por qué es recomendable...?, ¿qué ocurre si no se hace...?),
  * comparación (¿qué diferencia hay entre... y ...?),
  * casos prácticos (¿qué harías si...?, ¿en qué situación conviene...?),
  * consecuencias (¿qué puede pasar si...?, ¿qué problema se evita al...?),
  * buenas prácticas y advertencias,
  * interpretación de ejemplos o fragmentos del texto.
- Exprime al máximo el contenido: si hay muchos matices, genera muchas preguntas.
- Puedes reutilizar un mismo concepto con enfoques distintos (contextos, errores típicos, decisiones de diseño).
- COMO NORMA GENERAL, genera AL MENOS 30 pares pregunta-respuesta para este bloque,
  y más si el texto lo permite.
- Esta es la ronda {round_index} de generación para este mismo bloque de texto.
  NO repitas literalmente preguntas que ya habrías generado en rondas anteriores;
  busca nuevos ángulos, escenarios y comparaciones.
- Formato OBLIGATORIO: JSON Lines, cada línea:
  {{"question": "texto de la pregunta", "answer": "texto de la respuesta"}}

Texto:
\"\"\"{block}\"\"\"
""".strip()


# =========================
# PARSEO SEGURO DEL JSONL
# =========================

def parse_jsonl_from_llm(text: str) -> List[Dict[str, str]]:
    """
    Intenta extraer líneas JSON válidas del texto devuelto por el modelo.
    Ignora líneas vacías o mal formadas.
    """
    pairs: List[Dict[str, str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("- "):
            line = line[2:].strip()
        if line.startswith("* "):
            line = line[2:].strip()

        if not (line.startswith("{") and line.endswith("}")):
            if "{" in line and "}" in line:
                line = line[line.find("{"):line.rfind("}") + 1]
            else:
                continue

        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue

        q = obj.get("question")
        a = obj.get("answer")
        if isinstance(q, str) and isinstance(a, str):
            pairs.append({"question": q.strip(), "answer": a.strip()})

    return pairs


# =========================
# PREPARACIÓN DE CADA FICHERO (LECTURA + TROCEO)
# =========================

def prepare_blocks_for_file(path: str) -> List[str]:
    """
    Lee el fichero según su extensión, extrae texto útil y lo trocea en bloques.
    """
    print(f"\n[INFO] Preparando archivo: {path}")
    ext = os.path.splitext(path)[1].lower()

    raw_text = ""

    if ext in (".txt", ".md"):
        raw_text = read_text_file(path)
        if ext == ".md":
            raw_text = strip_markdown(raw_text)
    elif ext in (".html", ".htm"):
        raw_text = extract_text_from_html(path)
    elif ext == ".pdf":
        raw_text = extract_text_from_pdf(path)
    else:
        print(f"[WARN] Extensión no soportada (debería haberse filtrado antes): {ext}")
        return []

    if not raw_text or not raw_text.strip():
        print("[WARN] Archivo vacío o sin texto útil, se ignorará (0 bloques).")
        return []

    text = normalize_whitespace(raw_text)

    if not text.strip():
        print("[WARN] Tras normalizar espacios el archivo quedó vacío, se ignorará (0 bloques).")
        return []

    blocks = split_into_blocks(text)
    print(f"[INFO]   -> {len(blocks)} bloques detectados.")
    return blocks


# =========================
# LÓGICA PRINCIPAL POR BLOQUE
# =========================

def generate_qa_for_block(block: str) -> List[Dict[str, str]]:
    """
    Genera muchas Q/A para un bloque de texto, usando varias rondas
    de prompts fáciles e intermedios/avanzados, con control de duplicados.
    """
    all_pairs: List[Dict[str, str]] = []
    seen: set[Tuple[str, str]] = set()

    # --- RONDAS FÁCILES ---
    for r in range(1, ROUNDS_EASY + 1):
        try:
            easy_text = call_ollama(
                SYSTEM_PROMPT_QA,
                build_user_prompt_easy(block, round_index=r)
            )
            easy_pairs = parse_jsonl_from_llm(easy_text)

            for p in easy_pairs:
                key = (p["question"].strip().lower(), p["answer"].strip().lower())
                if key not in seen:
                    seen.add(key)
                    all_pairs.append(p)

        except Exception as e:
            print(f"\n[WARN] Error generando Q/A fáciles (ronda {r}): {e}")

    # --- RONDAS INTERMEDIAS / AVANZADAS ---
    for r in range(1, ROUNDS_ADVANCED + 1):
        try:
            adv_text = call_ollama(
                SYSTEM_PROMPT_QA,
                build_user_prompt_advanced(block, round_index=r)
            )
            adv_pairs = parse_jsonl_from_llm(adv_text)

            for p in adv_pairs:
                key = (p["question"].strip().lower(), p["answer"].strip().lower())
                if key not in seen:
                    seen.add(key)
                    all_pairs.append(p)

        except Exception as e:
            print(f"\n[WARN] Error generando Q/A avanzadas (ronda {r}): {e}")

    return all_pairs


# =========================
# PROCESAMIENTO DE UN FICHERO (GUARDADO SOBRE LA MARCHA)
# =========================

def process_single_file(path: str,
                        output_path: str,
                        blocks: List[str],
                        tracker: Optional[ProgressTracker],
                        file_index: int,
                        total_files: int) -> int:
    print(f"\n[INFO] Procesando archivo {file_index}/{total_files}: {path}")

    if not blocks:
        with open(output_path, "w", encoding="utf-8"):
            pass
        print("[INFO] Archivo sin bloques, JSONL vacío generado.")
        return 0

    # Crear/limpiar archivo de salida
    with open(output_path, "w", encoding="utf-8"):
        pass

    total_pairs_for_file = 0

    for block in blocks:
        block_pairs = generate_qa_for_block(block)

        if block_pairs:
            with open(output_path, "a", encoding="utf-8") as f:
                for p in block_pairs:
                    f.write(json.dumps(p, ensure_ascii=False) + "\n")

        total_pairs_for_file += len(block_pairs)

        if tracker is not None:
            tracker.update(
                step=1,
                prefix=f"[PROGRESO] Archivo {file_index}/{total_files}"
            )

    print(f"\n[INFO] Total pares Q/A para {os.path.basename(path)}: {total_pairs_for_file}")
    print(f"[INFO] JSONL generado para {path}: {output_path}")
    return total_pairs_for_file


# =========================
# GENERACIÓN DEL INFORME MARKDOWN
# =========================

def generate_markdown_report(
    processed_this_run: List[str],
    total_pairs_this_run: int,
    start_dt: datetime,
    end_dt: datetime,
) -> Optional[str]:
    """
    Genera un informe en Markdown en OUTPUT_DIR con toda la trazabilidad
    de la ejecución y el detalle de los pares Q/A generados en esta run.

    Devuelve la ruta completa del informe generado o None si no se generó.
    """
    if not processed_this_run:
        print("[INFO] No hay archivos procesados en esta ejecución; no se generará informe Markdown.")
        return None

    duration = end_dt - start_dt
    epoch = int(end_dt.timestamp())
    timestamp_str = end_dt.strftime("%Y%m%d_%H%M%S")
    report_name = f"reporte_QA_{timestamp_str}_{epoch}.md"
    report_path = os.path.join(OUTPUT_DIR, report_name)

    # Información del sistema
    system_info = {
        "Sistema operativo": platform.system(),
        "Versión del sistema": platform.version(),
        "Plataforma": platform.platform(),
        "Máquina": platform.machine(),
        "Procesador": platform.processor(),
        "Python": platform.python_version(),
        "Directorio de trabajo": os.getcwd(),
    }

    # Construcción del contenido Markdown
    lines: List[str] = []

    # Cabecera general
    lines.append("# Informe de generación de preguntas y respuestas\n")
    lines.append("## Resumen de la ejecución\n")
    lines.append(f"- **Fecha/hora de inicio:** {start_dt.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- **Fecha/hora de finalización:** {end_dt.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- **Duración total:** {duration}")
    lines.append(f"- **Modelo de Ollama utilizado:** `{MODEL_NAME}`")
    lines.append(f"- **Modo del endpoint de Ollama:** `{OLLAMA_MODE}`")
    lines.append(f"- **URL base de Ollama:** `{OLLAMA_BASE_URL}`")
    lines.append(f"- **Endpoint efectivo:** `{OLLAMA_URL}`")
    lines.append(f"- **Total de archivos procesados en esta ejecución:** {len(processed_this_run)}")
    lines.append(f"- **Total de pares Q/A generados en esta ejecución:** {total_pairs_this_run}")
    lines.append(f"- **Archivo de log global:** `{LOG_FILE}`")
    lines.append(f"- **Directorio de salida JSONL e informes:** `{OUTPUT_DIR}`\n")

    # Parámetros de configuración relevantes
    lines.append("## Parámetros de configuración utilizados\n")
    lines.append(f"- **MAX_CHARS_PER_BLOCK:** {MAX_CHARS_PER_BLOCK}")
    lines.append(f"- **BLOCK_OVERLAP:** {BLOCK_OVERLAP}")
    lines.append(f"- **TEMPERATURE:** {TEMPERATURE}")
    lines.append(f"- **MAX_TOKENS (num_predict):** {MAX_TOKENS}")
    lines.append(f"- **ROUNDS_EASY (rondas de preguntas fáciles):** {ROUNDS_EASY}")
    lines.append(f"- **ROUNDS_ADVANCED (rondas de preguntas avanzadas):** {ROUNDS_ADVANCED}")
    lines.append(f"- **Extensiones admitidas:** {', '.join(VALID_EXTS)}\n")

    # Información del sistema
    lines.append("## Información del sistema\n")
    for k, v in system_info.items():
        lines.append(f"- **{k}:** {v}")
    lines.append("")

    # Índice de archivos
    lines.append("## Índice de archivos procesados en esta ejecución\n")
    for idx, path in enumerate(processed_this_run, start=1):
        base = os.path.basename(path)
        lines.append(f"- [Archivo {idx}: `{base}`](#archivo-{idx})")
    lines.append("")

    # Detalle por archivo
    for idx, path in enumerate(processed_this_run, start=1):
        base_name = os.path.splitext(os.path.basename(path))[0]
        jsonl_path = os.path.join(OUTPUT_DIR, f"{base_name}.jsonl")

        # Anchor HTML para asegurar que el índice funcione en cualquier renderer
        lines.append(f"<a name=\"archivo-{idx}\"></a>")
        lines.append(f"## Archivo {idx}: `{base_name}`\n")
        lines.append(f"- **Archivo de entrada:** `{path}`")
        lines.append(f"- **Archivo JSONL generado:** `{jsonl_path}`")

        pairs: List[Dict[str, str]] = []
        if os.path.exists(jsonl_path):
            try:
                with open(jsonl_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                        except json.JSONDecodeError:
                            continue
                        q = obj.get("question")
                        a = obj.get("answer")
                        if isinstance(q, str) and isinstance(a, str):
                            pairs.append({"question": q, "answer": a})
            except Exception as e:
                lines.append(f"- **Aviso:** no se pudo leer el JSONL (`{e}`)")

        lines.append(f"- **Total de pares Q/A en este archivo:** {len(pairs)}\n")

        if pairs:
            lines.append("### Detalle de preguntas y respuestas\n")
            for i, p in enumerate(pairs, start=1):
                lines.append(f"**{i}. Pregunta:** {p['question']}")
                lines.append(f"   - **Respuesta:** {p['answer']}\n")
        else:
            lines.append("_Este archivo no contiene pares Q/A (JSONL vacío o ilegible)._")
            lines.append("")

    # Escritura a disco
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n[INFO] Informe Markdown generado: {report_path}")
    return report_path


# =========================
# MAIN
# =========================

def main():
    ensure_dirs()

    # Marca de tiempo de inicio
    start_dt = datetime.now()

    print("[INFO] Comprobando servicio de Ollama y detectando endpoint...")
    if not detect_ollama_mode():
        print("[FATAL] No se ha podido detectar un endpoint válido de Ollama. Abortando.")
        return

    # Recorre INPUT_DIR de forma recursiva
    input_files: List[str] = []
    for root, _, files in os.walk(INPUT_DIR):
        for fn in files:
            if fn.lower().endswith(VALID_EXTS):
                full_path = os.path.join(root, fn)
                input_files.append(full_path)

    if not input_files:
        print(f"[INFO] No se han encontrado ficheros válidos en {INPUT_DIR}.")
        print("      Extensiones admitidas:", ", ".join(VALID_EXTS))
        return

    log = load_log()
    processed_files_log = set(log.get("processed_files", []))

    pending_files = [p for p in sorted(input_files) if p not in processed_files_log]

    if not pending_files:
        print("[INFO] Todos los archivos presentes ya estaban procesados según log.json.")
        print(f"[INFO] Log de materiales procesados: {LOG_FILE}")
        # Marca de tiempo de fin y generación de informe vacío (no tiene sentido en este caso)
        end_dt = datetime.now()
        return

    # Primera pasada: preparar bloques por fichero y contar bloques totales
    print("\n[INFO] Calculando número total de bloques para la barra de progreso global...")
    file_blocks_map: Dict[str, List[str]] = {}
    total_blocks = 0

    for path in pending_files:
        blocks = prepare_blocks_for_file(path)
        file_blocks_map[path] = blocks
        total_blocks += len(blocks)

    if total_blocks == 0:
        print("[WARN] No se han encontrado bloques de texto útiles en los ficheros pendientes.")
        print("       Se actualizará el log, pero no se generarán Q/A.")
        newly_processed_count = 0
        processed_this_run: List[str] = []
        for path in pending_files:
            base_name = os.path.splitext(os.path.basename(path))[0]
            per_file_output = os.path.join(OUTPUT_DIR, f"{base_name}.jsonl")
            with open(per_file_output, "w", encoding="utf-8"):
                pass
            log.setdefault("processed_files", []).append(path)
            save_log(log)
            newly_processed_count += 1
            processed_this_run.append(path)

        end_dt = datetime.now()

        print("\n[RESUMEN]")
        print(f"Archivos encontrados              : {len(input_files)}")
        print(f"Archivos ya procesados (skip)     : {len(input_files) - len(pending_files)}")
        print(f"Archivos procesados en esta run   : {newly_processed_count}")
        print(f"Pares Q/A generados en esta run   : 0")
        print(f"Log de materiales procesados      : {LOG_FILE}")
        print(f"JSONL individuales en             : {OUTPUT_DIR}")

        # Informe (tendrá Q/A = 0, pero deja constancia de la ejecución)
        generate_markdown_report(
            processed_this_run=processed_this_run,
            total_pairs_this_run=0,
            start_dt=start_dt,
            end_dt=end_dt,
        )
        return

    tracker = ProgressTracker(total_blocks)

    total_pairs = 0
    newly_processed_count = 0
    skipped_count = len(input_files) - len(pending_files)
    processed_this_run: List[str] = []

    print(f"[INFO] Total de bloques a procesar: {total_blocks}")
    print("[INFO] Iniciando generación de Q/A con barra de progreso global...\n")

    for idx, path in enumerate(pending_files, start=1):
        base_name = os.path.splitext(os.path.basename(path))[0]
        per_file_output = os.path.join(OUTPUT_DIR, f"{base_name}.jsonl")

        blocks = file_blocks_map.get(path, [])
        pairs_count = process_single_file(
            path=path,
            output_path=per_file_output,
            blocks=blocks,
            tracker=tracker,
            file_index=idx,
            total_files=len(pending_files)
        )
        total_pairs += pairs_count

        log.setdefault("processed_files", []).append(path)
        save_log(log)
        newly_processed_count += 1
        processed_this_run.append(path)

    tracker.finish(prefix="[PROGRESO]")

    end_dt = datetime.now()

    print("\n[RESUMEN]")
    print(f"Archivos encontrados              : {len(input_files)}")
    print(f"Archivos ya procesados (skip)     : {skipped_count}")
    print(f"Archivos procesados en esta run   : {newly_processed_count}")
    print(f"Pares Q/A generados en esta run   : {total_pairs}")
    print(f"Log de materiales procesados      : {LOG_FILE}")
    print(f"JSONL individuales en             : {OUTPUT_DIR}")

    # Generación del informe Markdown al final de la ejecución
    generate_markdown_report(
        processed_this_run=processed_this_run,
        total_pairs_this_run=total_pairs,
        start_dt=start_dt,
        end_dt=end_dt,
    )


if __name__ == "__main__":
    main()

