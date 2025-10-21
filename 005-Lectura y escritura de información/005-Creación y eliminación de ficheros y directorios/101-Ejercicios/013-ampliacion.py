import os
import zipfile
import shutil
import sys
import time

#### CUIDADO CON ESTE PROGRAMA
#### USALO BIEN
#### UN GRAN PODER CONLLEVA UNA GRAN RESPONSABILIDAD

'''
  Quiero:
  1.-Pedir al usuario una ruta de una carpeta con input
  2.-Repasar todas las subcarpetas y archivos dentro de esa carpeta
  3.-Para cada archivo o carpeta, quiero comprimirla en un ZIP
  4.-Una vez comprimido ese zip, quiero eliminar los contenidos originales (opcional con booleano)
  5.-Mostrar una barra de progreso en consola con porcentaje y estimación de tiempo
'''

# 1) Booleano para activar/desactivar el borrado de originales
borrar_originales = False  # ponlo a False para conservar los originales

# ---- Utilidades para la barra de progreso ----
def formatear_tiempo(segundos):
  segundos = int(segundos)
  h = segundos // 3600
  m = (segundos % 3600) // 60
  s = segundos % 60
  if h > 0:
    return f"{h:02d}:{m:02d}:{s:02d}"
  else:
    return f"{m:02d}:{s:02d}"

def mostrar_progreso(procesados, total, inicio):
  if total == 0:
    return
  porcentaje = (procesados / total)
  ancho_barra = 30
  rellenos = int(ancho_barra * porcentaje)
  barra = "[" + "#" * rellenos + "-" * (ancho_barra - rellenos) + "]"

  transcurrido = time.time() - inicio
  if procesados > 0:
    estimado_total = transcurrido / procesados * total
    restante = max(0, estimado_total - transcurrido)
  else:
    restante = 0

  texto = f"\r{barra} {porcentaje*100:6.2f}%  transcurrido: {formatear_tiempo(transcurrido)}  restante: {formatear_tiempo(restante)}"
  sys.stdout.write(texto)
  sys.stdout.flush()
# ---------------------------------------------

ruta = input("Introduce la ruta de la carpeta: ").strip()

try:
  # Comprobamos que la ruta existe y es una carpeta
  if not os.path.isdir(ruta):
    print("La ruta no es válida")
  else:
    # Preparamos la lista de ítems a procesar (solo primer nivel), excluyendo ZIPs
    items = []
    for nombre in os.listdir(ruta):
      origen = os.path.join(ruta, nombre)
      if os.path.isfile(origen) and origen.lower().endswith(".zip"):
        continue
      items.append(origen)

    total = len(items)
    procesados = 0
    inicio = time.time()
    mostrar_progreso(procesados, total, inicio)

    for origen in items:
      nombre = os.path.basename(origen)

      # Si es una carpeta: crear un ZIP con todo su contenido
      if os.path.isdir(origen):
        destino = origen + ".zip"
        archivozip = zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED)
        for directorio, subcarpetas, archivos in os.walk(origen):
          for archivo in archivos:
            rutaarchivo = os.path.join(directorio, archivo)
            rutarelativa = os.path.relpath(rutaarchivo, origen)
            archivozip.write(rutaarchivo, rutarelativa)
        archivozip.close()

        # Borrar carpeta original si está activado
        if borrar_originales:
          shutil.rmtree(origen)

      # Si es un archivo: comprimirlo
      elif os.path.isfile(origen):
        destino = origen + ".zip"
        archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
        archivo.write(origen, arcname=nombre)
        archivo.close()

        # Borrar archivo original si está activado
        if borrar_originales:
          os.remove(origen)

      # Actualizamos progreso
      procesados += 1
      mostrar_progreso(procesados, total, inicio)

    print()  # salto de línea al terminar la barra
    print("Proceso completado.")

except:
  print("\nHa habido un error, continuamos")

