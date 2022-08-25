import tkinter as tk

class Aplicacion_slider:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Aplicacion slider')

        self.vertical = tk.Scale(self.ventana, from_=0, to=400)
        self.vertical.pack()

        self.horizontal = tk.Scale(self.ventana, from_=0, to=400, orient=tk.HORIZONTAL)
        self.horizontal.pack()

        self.btn_tamano = tk.Button(self.ventana, text='Click me!', command=self.tamano)
        self.btn_tamano.pack()

        self.ventana.mainloop()

    def tamano(self):
        self.ventana.geometry(str(self.horizontal.get()) + 'x' + str(self.vertical.get()))
        self.lbl_tamano = tk.Label(self.ventana, text=str(self.horizontal.get()) + 'x' + str(self.vertical.get()))
        self.lbl_tamano.pack()

aplicacion1 = Aplicacion_slider()
