from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Learn to code')
root.iconbitmap('snake.ico')

# global mylabel

r = IntVar()
# r.set('2')

# mylabel = Label(root, text=r.get())
# mylabel.pack()


Radiobutton(root, text='opcion1', variable=r, value=1).pack()
Radiobutton(root, text='opcion2', variable=r, value=2).pack()


def clicked():
    mylabel = Label(root, text=r.get())
    mylabel.pack()
    # mylabel.config(text=value)

seleccion = Button(root, text='Select', command=clicked).pack()

root.mainloop()

#NOTA: con este ejemplo la respuesta se obtiene presionando un boton.
