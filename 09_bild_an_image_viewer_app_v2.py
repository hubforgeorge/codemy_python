import tkinter as tk
from PIL import ImageTk, Image

class Visor:
    def __init__(self):

        self.root=tk.Tk()
        self.root.title('Learn to code')
        self.root.iconbitmap('snake.ico')
        self.n = 0


        my_img1 = ImageTk.PhotoImage(Image.open('imagenes/mano.jpg'))
        my_img2 = ImageTk.PhotoImage(Image.open('imagenes/mariposa.jpg'))
        my_img3 = ImageTk.PhotoImage(Image.open('imagenes/marrano.jpg'))
        my_img4 = ImageTk.PhotoImage(Image.open('imagenes/mazorca.jpg'))
        my_img5 = ImageTk.PhotoImage(Image.open('imagenes/pez.jpg'))
        my_img6 = ImageTk.PhotoImage(Image.open('imagenes/pipa.jpg'))
        my_img7 = ImageTk.PhotoImage(Image.open('imagenes/molino.jpg'))
        my_img8 = ImageTk.PhotoImage(Image.open('imagenes/momia.jpg'))
        my_img9 = ImageTk.PhotoImage(Image.open('imagenes/monedero.jpg'))
        my_img10 = ImageTk.PhotoImage(Image.open('imagenes/mula.jpg'))
        my_img11 = ImageTk.PhotoImage(Image.open('imagenes/pelota.jpg'))
        my_img12 = ImageTk.PhotoImage(Image.open('imagenes/pera.jpg'))

        self.image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img11, my_img12]

        self.my_label = tk.Label(self.root, image=self.image_list[self.n])
        self.my_label.grid(column=0, row=0, columnspan=3)

        self.lbl_contador = tk.Label(self.root, text=str(self.n+1))
        self.lbl_contador.grid(column=0, row=1, columnspan=3)

        self.button_back = tk.Button(self.root, text='<<', command=self.back)
        self.button_exit = tk.Button(self.root, text='Exit program', command=self.root.quit)
        self.button_forward = tk.Button(self.root, text='>>', command=self.forward)    #se le da al boton un valor inicial, luego back y forward se llamaran recursivamente

        self.button_back.grid(column=0, row=2)
        self.button_exit.grid(column=1, row=2)
        self.button_forward.grid(column=2, row=2)

        self.root.mainloop()

    def forward(self):
        self.n += 1
        if self.n < len(self.image_list):
            self.my_label.grid_forget()
            self.my_label = tk.Label(self.root, image=self.image_list[self.n])
            self.my_label.grid(column=0, row=0, columnspan=3)
        else:
            self.n -= 1
        self.lbl_contador.config(text=str(self.n + 1))

    def back(self):
        self.n -= 1
        if self.n >= 0:
            self.my_label.grid_forget()
            self.my_label = tk.Label(self.root, image=self.image_list[self.n])
            self.my_label.grid(column=0, row=0, columnspan=3)
        else:
            self.n += 1
        self.lbl_contador.config(text=str(self.n + 1))



visor1 = Visor()
