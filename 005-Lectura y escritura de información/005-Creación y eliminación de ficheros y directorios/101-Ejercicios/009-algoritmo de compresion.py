import zipfile

origen = 'crmca_crmcapitol (1).sql'

destino = 'basededatos.zip'

archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
archivo.write(origen)



