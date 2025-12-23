from flask import Flask, render_template, request, jsonify
import subprocess
import threading
import queue
import uuid
import os
import tempfile

app = Flask(__name__)

# Almacenar sesiones de procesos
sessions = {}

class PythonSession:
    def __init__(self, code: str):
        # Guardamos el código en un archivo temporal
        fd, path = tempfile.mkstemp(suffix=".py", prefix="compilador_")
        os.write(fd, code.encode("utf-8"))
        os.close(fd)

        self.path = path
        self.proc = subprocess.Popen(
            ["python3", self.path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,  # line-buffered
        )
        self.queue = queue.Queue()
        self.alive = True

        # Hilo que lee stdout + stderr y los mete en la cola
        self.thread = threading.Thread(target=self._reader_thread, daemon=True)
        self.thread.start()

    def _reader_thread(self):
        try:
            for line in self.proc.stdout:
                self.queue.put(line)
            # cuando stdout se cierra, leemos también stderr restante
            err = self.proc.stderr.read()
            if err:
                self.queue.put(err)
        finally:
            self.proc.wait()
            self.alive = False
            # limpiar archivo temporal
            try:
                os.remove(self.path)
            except OSError:
                pass

    def write(self, data: str):
        if not self.alive:
            return
        try:
            self.proc.stdin.write(data + "\n")
            self.proc.stdin.flush()
        except Exception:
            self.alive = False

    def read_all(self) -> str:
        chunks = []
        while not self.queue.empty():
            try:
                chunks.append(self.queue.get_nowait())
            except queue.Empty:
                break
        return "".join(chunks)

    def is_alive(self) -> bool:
        return self.alive and self.proc.poll() is None


@app.route("/")
def inicio():
    return render_template("frentemasampliado.html")


@app.route("/api/start", methods=["POST"])
def api_start():
    data = request.get_json(force=True)
    code = data.get("code", "")

    session_id = str(uuid.uuid4())
    sessions[session_id] = PythonSession(code)

    return jsonify({"session_id": session_id})


@app.route("/api/write", methods=["POST"])
def api_write():
    data = request.get_json(force=True)
    session_id = data.get("session_id")
    line = data.get("line", "")

    sess = sessions.get(session_id)
    if not sess:
        return jsonify({"error": "Sesión no encontrada"}), 404

    sess.write(line)
    return jsonify({"ok": True})


@app.route("/api/read", methods=["GET"])
def api_read():
    session_id = request.args.get("session_id")
    sess = sessions.get(session_id)
    if not sess:
        return jsonify({"error": "Sesión no encontrada"}), 404

    output = sess.read_all()
    alive = sess.is_alive()

    # Si el proceso ha terminado y no queda nada que leer, limpiar la sesión
    if not alive and not output:
        sessions.pop(session_id, None)

    return jsonify({"output": output, "alive": alive})


if __name__ == "__main__":
    app.run(debug=True)
