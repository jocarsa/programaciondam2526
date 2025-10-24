import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=20,pady=20)

marco.pack(padx=20,pady=20)

ventana.mainloop()
