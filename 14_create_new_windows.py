from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code')
# root.iconbitmap('snake.ico')

def open():
    global my_img
    top = Toplevel()
    top.title('My second window')
    my_img = ImageTk.PhotoImage(Image.open('pulga.png'))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='Close window', command=top.destroy).pack()

btn = Button(root, text='Open second window', command=open).pack()

root.mainloop()


Nota:
para que sea visible la imagen se tiene que declarar la variabel contenedora como global
