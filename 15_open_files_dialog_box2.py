import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

class Abrir_ventana_app:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Aplicacion para abrir una ventana')

        btn_abrir = tk.Button(self.ventana, text='Seleccione un archivo', command=self.abrir)
        btn_abrir.pack()

        self.ventana.mainloop()

    def abrir(self):
        global arc_imagen
        archivo = filedialog.askopenfilename(initialdir='/home/jorge/Documentos/codemy_python', title='Seleccione el archivo', filetypes=(('Archivos png','*.png'),('Todos los archivos','*.*')))
        arc_imagen = ImageTk.PhotoImage(Image.open(archivo))
        lbl_ubicacion = tk.Label(self.ventana, text=archivo).pack()

        lbl_imagen = tk.Label(self.ventana, image=arc_imagen).pack()

ventana1 = Abrir_ventana_app()
