# pip3 install ttkbootsrap --break-system-packages
import tkinter as tk
from tkinter import ttk
import mysql.connector
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# --- Database connection ---
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()

# --- Main window setup ---
ventana = tb.Window(themename="superhero")  # try also: "minty", "flatly", "darkly"
ventana.title("Gestión de Clientes")
ventana.geometry("800x600")

# --- Frames layout ---
frame_form = ttk.LabelFrame(ventana, text="Nuevo cliente", padding=20)
frame_form.pack(fill=X, padx=20, pady=10)

frame_tabla = ttk.LabelFrame(ventana, text="Lista de clientes", padding=20)
frame_tabla.pack(fill=BOTH, expand=True, padx=20, pady=10)

# --- Form fields ---
def insertar():
    dni = dninie.get()
    nom = nombre.get()
    ape = apellidos.get()
    ema = email.get()

    if dni == "" or nom == "" or ape == "" or ema == "":
        tb.dialogs.Messagebox.show_warning("Por favor, completa todos los campos", title="Atención")
        return

    cursor.execute('''
        INSERT INTO clientes VALUES (NULL, %s, %s, %s, %s);
    ''', (dni, nom, ape, ema))
    conexion.commit()
    cargar_datos()
    tb.dialogs.Messagebox.show_info("Cliente insertado correctamente", title="Éxito")

    # Limpiar campos
    dninie.delete(0, tk.END)
    nombre.delete(0, tk.END)
    apellidos.delete(0, tk.END)
    email.delete(0, tk.END)

# Form fields (left to right layout)
ttk.Label(frame_form, text="DNI/NIE:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
dninie = ttk.Entry(frame_form, width=20)
dninie.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, padx=5, pady=5, sticky=W)
nombre = ttk.Entry(frame_form, width=20)
nombre.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(frame_form, text="Apellidos:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
apellidos = ttk.Entry(frame_form, width=20)
apellidos.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Email:").grid(row=1, column=2, padx=5, pady=5, sticky=W)
email = ttk.Entry(frame_form, width=20)
email.grid(row=1, column=3, padx=5, pady=5)

ttk.Button(frame_form, text="Insertar cliente", command=insertar, bootstyle=SUCCESS).grid(
    row=0, column=4, rowspan=2, padx=10, pady=5, sticky=NS
)

# --- Treeview setup ---
columnas = ("dninie", "nombre", "apellidos", "email")
arbol = ttk.Treeview(frame_tabla, columns=columnas, show="headings", bootstyle=INFO)
for col in columnas:
    arbol.heading(col, text=col.capitalize())
    arbol.column(col, width=180, anchor=W)

# Scrollbars
scroll_y = ttk.Scrollbar(frame_tabla, orient=VERTICAL, command=arbol.yview)
scroll_x = ttk.Scrollbar(frame_tabla, orient=HORIZONTAL, command=arbol.xview)
arbol.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

arbol.grid(row=0, column=0, sticky=NSEW)
scroll_y.grid(row=0, column=1, sticky=NS)
scroll_x.grid(row=1, column=0, sticky=EW)

frame_tabla.rowconfigure(0, weight=1)
frame_tabla.columnconfigure(0, weight=1)

# --- Function to load data into the table ---
def cargar_datos():
    cursor.execute("SELECT * FROM clientes;")
    filas = cursor.fetchall()
    arbol.delete(*arbol.get_children())
    for fila in filas:
        arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))

# --- Initial load ---
cargar_datos()

ventana.mainloop()

