# Non Playable Character

class Npc():
  def __init__(self,x,y):
    self.posx = x
    self.posy = y
    
personajes = []
numero_personajes = 50

for i in range(0,numero_personajes):
	personajes.append(Npc(4,3))

print(personajes)