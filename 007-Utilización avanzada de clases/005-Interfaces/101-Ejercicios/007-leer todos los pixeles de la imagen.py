from PIL import Image

imagen = Image.open("josevicente.jpg")

anchura,altura = imagen.size		# Cojo altura y anchura

for x in range(0,anchura):			# Repaso la anchura
	for y in range(0,altura):			# Repaso la altura
		pixel = imagen.getpixel((x, y))	# Cojo cada pixel
		print(pixel)										# Y lo saco por pantalla