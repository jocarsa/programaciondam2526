import os

carpeta = input("Indica una carpeta: ")
grande = 1024*1024*1024 # 1 giga

mapa = open("mapa.txt",'w') # Vaciamos los contenidos anteriores

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        mapa.write(ruta+"\n")
        
mapa.close()
         
    
