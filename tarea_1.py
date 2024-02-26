from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor

"""
Ejercicio unidad 6 1
Elias Escalante

A partir del ejercicio desafío de la unidad anterior cree una aplicación que permita realizar un alta de registros en un diccionario dentro de la app

"""



# definicion de las funciones alta y sorpresa


# la funcion de alta imprime en consola los datos ingresados en los entry
def alta():
    base_datos_dic =  {"Titulo": titulo_var.get(), "Descripción": descripcion_var.get()}
    print("datos ingresados: \n")
    print(base_datos_dic)


# la funcion sorpresa muestra un mensaje de error en una ventana emergente
def sorpresa():
    showerror("Título de mensaje de error", "No entendi que hay que hacer ...XD")

def color():
    result = askcolor(color="#00ff00",title="Bernd´s Colour Chooser")
    root.configure(bg=result[1])



# Inicio de la app
root = Tk()



# definicion de variables para asignar las entradas
titulo_var = StringVar()
descripcion_var = StringVar()


# Establecer el título de la ventana
root.title("Tarea unidad 5")

# Configurar la cuadrícula para que el widget se expanda horizontalmente
root.columnconfigure(3, weight=1)

# Configurar el label_banner para que ocupe toda la ventana (lo intente)
label_banner = Label(root, text="Ingresa tu información", font=('Arial', 12), bg="blue", fg="white")
label_banner.grid(row=0, column=3, columnspan=2, sticky="ew")


# Agrego el label y el entry para "el titulo"
titulo = Label(root, text="Titulo")
titulo.grid(row=2, column=0, sticky="e", padx=1, pady=10)
entry_titulo = Entry(root, textvariable=titulo_var, width=25)
entry_titulo.grid(row=2, column=3, sticky="e", padx=5, pady=10)

# Agrego el label y el entry para "Descripción"
descripcion = Label(root, text="Descripción")
descripcion.grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_descripcion = Entry(root, textvariable=descripcion_var, width=25)
entry_descripcion.grid(row=4, column=3, sticky="e", padx=5, pady=5)


# agrego los botones
boton_agregar = Button(root, text="Alta", command=alta)
boton_agregar.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# agrego boton sorpresa
boton_sorpresa =  Button(root, text="Sorpresa", command=sorpresa)
boton_sorpresa.grid(row=6, column=4, columnspan=2, padx=5, pady=5)

# agrego boton sorpresa 2
boton_sorpresa_1 = Button(root, text="Sorpresa 2", command=color)
boton_sorpresa_1.grid(row=7, column=4, columnspan=2, padx=5, pady=5)


# Establecer el tamaño de la ventana
root.geometry("400x200")

# Entrar en el bucle principal de Tkinter
root.mainloop()