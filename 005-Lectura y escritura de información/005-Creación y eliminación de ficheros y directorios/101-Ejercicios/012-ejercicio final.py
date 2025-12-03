import os
import zipfile
import shutil

'''
  Quiero:
  1.-Pedir al usuario una ruta de una carpeta con input
  2.-Repasar todas las subcarpetas y archivos dentro de esa carpeta
  3.-Para cada archivo o carpeta, quiero comprimirla en un ZIP
  4.-Una vez comprimido ese zip, quiero eliminar los contenidos originales
'''

ruta = input("Introduce la ruta de la carpeta: ").strip()

try:
  # Comprobamos que la ruta existe y es una carpeta
  if not os.path.isdir(ruta):
    print("La ruta no es válida")
  else:
    # Recorremos SOLO el primer nivel dentro de la ruta dada
    for nombre in os.listdir(ruta):
      origen = os.path.join(ruta, nombre)

      # Evitar recomprimir ZIPs ya existentes
      if os.path.isfile(origen) and origen.lower().endswith(".zip"):
        continue

      # Si es una carpeta: crear un ZIP con todo su contenido y luego eliminarla
      if os.path.isdir(origen):
        destino = origen + ".zip"
        archivozip = zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED)
        for directorio, subcarpetas, archivos in os.walk(origen):
          for archivo in archivos:
            rutaarchivo = os.path.join(directorio, archivo)
            rutarelativa = os.path.relpath(rutaarchivo, origen)
            archivozip.write(rutaarchivo, rutarelativa)
        archivozip.close()
        shutil.rmtree(origen)

      # Si es un archivo: comprimirlo y luego eliminar el original
      elif os.path.isfile(origen):
        destino = origen + ".zip"
        archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
        archivo.write(origen, arcname=nombre)
        archivo.close()
        os.remove(origen)

except:
  print("Ha habido un error, continuamos")

