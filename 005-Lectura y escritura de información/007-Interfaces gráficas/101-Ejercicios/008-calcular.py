# sudo apt-get install python3-tk
import tkinter as tk

def calcular():
  op1valor = float(operando1.get())
  op2valor = float(operando2.get())
  suma = op1valor + op2valor
  resultado.config(text=str(suma))

ventana = tk.Tk()

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Calcular!",command=calcular)
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Aqui va el resultado")
resultado.pack(padx=10,pady=10)

ventana.mainloop() # No te salgas
