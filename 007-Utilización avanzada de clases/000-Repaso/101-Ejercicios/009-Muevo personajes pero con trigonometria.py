import random
import json
from flask import Flask,render_template
import math # Para poder hacer trigonometria

class Npc():
	def __init__(self, x, y,radio,direccion):
		self.posx = x
		self.posy = y
		self.radio = radio
		self.direccion = direccion # NUEVO

	def to_dict(self):
		return {
      "posx": self.posx, 
      "posy": self.posy,
      "radio": self.radio,
    	"direccion": self.direccion # NUEVO
    }
	def mover(self):
		self.posx += math.cos(self.direccion) # NUEVO
		self.posy += math.sin(self.direccion) # NUEVO
# Preparo los personajes

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
	xaleatoria = random.randint(0, 500)
	yaleatoria = random.randint(0, 500)
	radioaleatorio = random.randint(10, 30)
	direccionaleatoria = random.random()*math.pi*2  # NUEVO
	personajes.append(
    Npc(xaleatoria, yaleatoria,radioaleatorio,direccionaleatoria) # NUEVO
  )



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
  
  
  
  
