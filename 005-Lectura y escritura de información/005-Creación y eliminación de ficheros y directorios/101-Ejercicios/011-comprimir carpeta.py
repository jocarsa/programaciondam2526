import os
import zipfile

origen = "archivos"
destino = "archivos.zip"

archivozip = zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED)
for directorio, carpetas, archivos in os.walk(origen):
  for archivo in archivos:
    rutaarchivo = os.path.join(directorio, archivo)
    rutarelativa = os.path.relpath(rutaarchivo, origen)
    archivozip.write(rutaarchivo, rutarelativa)
    
archivozip.close()

