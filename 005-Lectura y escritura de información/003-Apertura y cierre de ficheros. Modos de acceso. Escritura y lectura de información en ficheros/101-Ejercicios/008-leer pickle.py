#pip3 install pickle | pip install pickle
import pickle

archivo = open("datos.bin","rb")

cadena = pickle.load(archivo)
print(cadena)

archivo.close()

