import tkinter as tk

class Aplicacion_OptionMenu:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Option menu')
        self.ventana.geometry('400x400')
        self.var = tk.StringVar()

        self.opciones = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
        self.var.set(self.opciones[0])

        self.opt_menu = tk.OptionMenu(self.ventana, self.var, *self.opciones)
        self.opt_menu.pack()

        self.btn_mostrar = tk.Button(self.ventana, text='Mostrar', command=self.mostrar)
        self.btn_mostrar.pack()

        self.ventana.mainloop()

    def mostrar(self):
        self.lbl_mostrar = tk.Label(self.ventana, text=self.var.get())
        self.lbl_mostrar.pack()

ventana1 = Aplicacion_OptionMenu()
