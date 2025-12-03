# Non Playable Character

class Npc():
  def __init__(self,x,y):
    self.posx = x
    self.posy = y
    
personajes = []

personajes.append(Npc(4,3))
personajes.append(Npc(3,4))

print(personajes)
