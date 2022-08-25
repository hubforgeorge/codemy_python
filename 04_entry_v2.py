import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.operacion()

        self.ventana.mainloop()

    def operacion(self):
        self.e = tk.Entry(self.ventana, width=20)
        self.e.pack()


        boton = tk.Button(self.ventana, text='click', command=self.etiqueta)
        boton.pack()


    def etiqueta(self):
        label = tk.Label(self.ventana, text='Hello, ' + self.e.get())
        label.pack()

aplicacion1 = Aplicacion()
