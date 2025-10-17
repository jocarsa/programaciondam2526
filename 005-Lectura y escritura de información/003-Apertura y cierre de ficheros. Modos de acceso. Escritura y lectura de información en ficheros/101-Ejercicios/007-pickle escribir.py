#pip3 install pickle | pip install pickle
import pickle

archivo = open("datos.bin","wb")
cadena = "Jose Vicente"

pickle.dump(cadena,archivo)

archivo.close()
