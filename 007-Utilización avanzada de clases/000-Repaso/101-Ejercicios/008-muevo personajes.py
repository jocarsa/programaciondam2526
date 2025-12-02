import random
import json
from flask import Flask,render_template

class Npc():
	def __init__(self, x, y,radio):
		self.posx = x
		self.posy = y
		self.radio = radio

	def to_dict(self):
		return {"posx": self.posx, "posy": self.posy,"radio":self.radio}
	def mover(self):
		self.posx += random.randint(-5,5)	# Muevete un poco en X
		self.posy += random.randint(-5,5)	# Muevete un poco en Y
# Preparo los personajes

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
	xaleatoria = random.randint(0, 500)
	yaleatoria = random.randint(0, 500)
	radioaleatorio = random.randint(10, 30)
	personajes.append(Npc(xaleatoria, yaleatoria,radioaleatorio))



# Lanzo una web

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("juego.html")

@app.route("/api")
def api():
  # Primero muevo todos los personajes
  for personaje in personajes:	
    personaje.mover()
  personajes_json = [p.to_dict() for p in personajes]
  return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
  app.run(debug=True)
  
  
  
  
