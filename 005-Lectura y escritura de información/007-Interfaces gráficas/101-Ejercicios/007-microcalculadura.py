# sudo apt-get install python3-tk
import tkinter as tk

ventana = tk.Tk()

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Calcular!")
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Aqui va el resultado")
resultado.pack(padx=10,pady=10)

ventana.mainloop() # No te salgas
