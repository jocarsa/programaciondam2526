from PIL import Image

imagen = Image.open("josevicente.jpg")

tamanio = imagen.size
print(tamanio)

pixel1 = imagen.getpixel((0, 0))

print(pixel1)
