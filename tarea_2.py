from tkinter import *
from tkinter.messagebox import *
import mysql.connector
import sqlite3

"""
A partir del ejercicio desafío de la unidad anterior cree una aplicación que permita realizar un alta de registros en la base de datos (sqlite3) 
"""

# definicion de funcion
def alta():
    # obtengo los valores de los campos de entrada
    nombre = nombre_var.get()
    apellido = apellido_var.get()
    
    # valido que los campos no estén vacíos
    if nombre == "" or apellido == "":
        showerror("Error", "Por favor, completa todos los campos.")
        return
    
    try:
        # conecto  la base de datos
        conexion = sqlite3.connect('mibase.db')
        cursor = conexion.cursor()
        
        # ejecuto la sentencia SQL para insertar el nuevo alumno
        cursor.execute("INSERT INTO alumno (nombre, apellido) VALUES (?, ?)", (nombre, apellido))
        
        # Confirmo la transacción
        conexion.commit()
        
        # cierro la conexión
        conexion.close()
        
        # muestro un mensaje de éxito
        showinfo("Éxito", "Alumno agregado correctamente.")
        
        # limpio los campos de entrada
        nombre_var.set("")
        apellido_var.set("")
        
    except Exception as e:
        # Mostrar un mensaje de error si ocurre algún problema
        showerror("Error", f"No se pudo agregar el alumno: {e}")


# Inicio de la app
app = Tk()

# definicion de variables para asignar las entradas
nombre_var = StringVar()
apellido_var = StringVar()

# maquetación de los widget
app.title("Tarea 1 - alta en una base de datos")

# Configurar la cuadrícula para que el widget se expanda horizontalmente
app.columnconfigure(3, weight=1)
# indico el tamaño de la ventana
app.geometry("400x150")

# Configurar el label_banner para que ocupe toda la ventana
label_banner = Label(app, text="Ingresa tu información para dar el alta", font=('Arial', 12), bg="blue", fg="white")
label_banner.grid(row=0, column=2, columnspan=2, sticky="ew")

# Agrego el label y el entry para "el nombre"
titulo = Label(app, text="Nombre")
titulo.grid(row=2, column=2, sticky="e", padx=2, pady=10)
entry_titulo = Entry(app, textvariable=nombre_var, width=25)
entry_titulo.grid(row=2, column=3, sticky="w", padx=5, pady=10)

# Agrego el label y el entry para "apellido"
descripcion = Label(app, text="Apellido")
descripcion.grid(row=3, column=2, sticky="e", padx=2, pady=10)
entry_descripcion = Entry(app, textvariable=apellido_var, width=25)
entry_descripcion.grid(row=3, column=3, sticky="w", padx=5, pady=10)

# Boton "Agregar alumno"
boton_agregar = Button(app, text="Agregar Alumno", command=alta)
boton_agregar.grid(row=5, column=2, sticky="w", padx=30, pady=5)

# Agrego boton para salir
salir = Button(app, text="Salir", command=lambda: app.quit())
salir.grid(row=5, column=3, sticky="e", padx=80, pady=5)



# cierre de la app
app.mainloop()