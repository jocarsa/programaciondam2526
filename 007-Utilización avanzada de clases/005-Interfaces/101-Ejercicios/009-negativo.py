# pip3 install pillow --break-system-packages
from PIL import Image

imagen = Image.open("josevicente.jpg")

anchura,altura = imagen.size	

for x in range(0,anchura):	
	for y in range(0,altura):	
		pixel = imagen.getpixel((x, y))	
		rojo = pixel[0]
		verde = pixel[1]
		azul = pixel[2]
		rojo = 255 - rojo					# Rojo a negativo
		verde = 255 - verde				# Verde a negativo
		azul = 255 - azul					# Azul a negativo
		imagen.putpixel((x, y), (rojo, verde, azul)) # ESTO ES CORRECTO
    
imagen.save("modificado.jpg")