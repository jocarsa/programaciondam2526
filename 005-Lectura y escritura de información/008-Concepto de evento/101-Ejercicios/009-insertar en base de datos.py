import tkinter as tk
import mysql.connector
conexion = mysql.connector.connect(host="localhost",user="empresadam",password="Empresadam123$",database="empresadam")
cursor = conexion.cursor()
ventana = tk.Tk()
def insertar():
  cursor.execute('''
    INSERT INTO clientes
    VALUES(
      NULL,
      "'''+dninie.get()+'''",
      "'''+nombre.get()+'''",
      "'''+apellidos.get()+'''",
      "'''+email.get()+'''"
    );
  ''')
  conexion.commit()
marco = tk.Frame(ventana)
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=10,pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=10,pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce el email del cliente").pack(padx=10,pady=10)
email = tk.Entry(marco)
email.pack(padx=10,pady=10)
tk.Button(marco,text="Insertar cliente",command = insertar).pack(padx=10,pady=10)
marco.pack(padx=20,pady=20)
ventana.mainloop()
