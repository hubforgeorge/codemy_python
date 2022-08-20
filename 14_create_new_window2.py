import tkinter as tk
from PIL import ImageTk, Image

class NewWindowApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Aplicacion ventana secundaria')

        btn_abrir = tk.Button(self.ventana, text='Mostrar imagen', command=self.foto)
        btn_abrir.pack()


        self.ventana.mainloop()

    def foto(self):

        global imagen1  #esta es la variable contenedora de la imagen
        top_foto = tk.Toplevel(self.ventana)
        imagen1 = ImageTk.PhotoImage(Image.open('pulga.png'))
        lbl_imagen = tk.Label(top_foto, image=imagen1)
        lbl_imagen.pack()

        btn2 = tk.Button(top_foto, text='Cerrar ventana', command=top_foto.destroy).pack()



newwindow2 = NewWindowApp()

# NOTA
# Para que funcione, se debe declarar como variable global la variable contenedora de la foto
