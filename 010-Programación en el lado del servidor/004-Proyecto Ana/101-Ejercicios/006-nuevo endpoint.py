from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("frente.html")

@app.route("/api")
def api():
  print("He recibido algo")
  return "ok"

if __name__ == "__main__":
  app.run(debug=True)
