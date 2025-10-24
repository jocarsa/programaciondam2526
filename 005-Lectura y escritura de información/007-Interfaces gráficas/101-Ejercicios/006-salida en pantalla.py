# sudo apt-get install python3-tk
import tkinter as tk

def accion():
  etiqueta.config(text="Pues sí que has pulsado el botón")

ventana = tk.Tk()

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10)

etiqueta = tk.Label(text="¿Has pulsado el botón?")
etiqueta.pack(padx=10,pady=10)

ventana.mainloop() # No te salgas
