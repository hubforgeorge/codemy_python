# import tkinter as tk

# class Aplicacion:
#     def __init__(self):
#         ventana = tk.Tk()

#         ventana.mainloop()


# aplicacion1 = Aplicacion()

# SEGUNDA OPCION COMO FUNCIONES

from tkinter import *



root = Tk()

def etiqueta():
    label = Label(root, text='se ha presionado un botón')
    label.pack()

boton = Button(root, text='aceptar', command=etiqueta, fg='white', bg='red')
boton.pack()

root.mainloop()
