print("Tres en raya - 2 jugadores humanos")
print("(c) 2025 Jose Vicente Carratala")

jugador = 1
casilla1 = 1
casilla2 = 2
casilla3 = 3
casilla4 = 4
casilla5 = 5
casilla6 = 6
casilla7 = 7
casilla8 = 8
casilla9 = 9

while True:
  print(f'{casilla1}|{casilla2}|{casilla3}')
  print(f'------')
  print(f'{casilla4}|{casilla5}|{casilla6}')
  print(f'------')
  print(f'{casilla7}|{casilla8}|{casilla9}')
  tirada = input("Tirada del jugador "+str(jugador))
  if int(tirada) == 1:
    if jugador == 1:
      casilla1 = "X"
    else:
      casilla1 = "O"
  if int(tirada) == 2:
    if jugador == 1:
      casilla2 = "X"
    else:
      casilla2 = "O"
  if int(tirada) == 3:
    if jugador == 1:
      casilla3 = "X"
    else:
      casilla3 = "O"
  if int(tirada) == 4:
    if jugador == 1:
      casilla4 = "X"
    else:
      casilla4 = "O"
  if int(tirada) == 5:
    if jugador == 1:
      casilla5 = "X"
    else:
      casilla5 = "O"
  if int(tirada) == 6:
    if jugador == 1:
      casilla6 = "X"
    else:
      casilla6 = "O"
  if int(tirada) == 7:
    if jugador == 1:
      casilla7 = "X"
    else:
      casilla7 = "O"
  if int(tirada) == 8:
    if jugador == 1:
      casilla8 = "X"
    else:
      casilla8 = "O"
  if int(tirada) == 9:
    if jugador == 1:
      casilla9 = "X"
    else:
      casilla9 = "O"
  if jugador == 1:
    jugador = 2
  else:
    jugador = 1
  
