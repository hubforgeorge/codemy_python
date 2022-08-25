import tkinter as tk

class Aplicacion_Checkbox:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Aplicacion checkbox')
        self.ventana.geometry('400x400')

        # self.var = tk.IntVar()
        # c = tk.Checkbutton(self.ventana, text='Check me!', variable=self.var)
        # c.pack()

        self.var = tk.StringVar()
        # self.var.set('Cheese')
        c = tk.Checkbutton(self.ventana, text='Check me if you want Pizza!', variable=self.var, onvalue='Pizza', offvalue='Cheese')
        c.deselect()    #se tiene que establecer 'deselect()' por que sino ocurre un error, la otra opcion es asignar un valor por defecto luego de declarar la variable
        c.pack()

        btn = tk.Button(self.ventana, text='Seleccion', command=self.show)
        btn.pack()



        self.ventana.mainloop()

    def show(self):
        lbl_mensaje = tk.Label(self.ventana, text=self.var.get())
        lbl_mensaje.pack()

ventana1 = Aplicacion_Checkbox()
