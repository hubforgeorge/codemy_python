from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Learn to code')
root.iconbitmap('snake.ico')

global mylabel

r = IntVar()
r.set('2')

mylabel = Label(root, text=r.get())
mylabel.pack()


Radiobutton(root, text='opcion1', variable=r, value=1, command=lambda:clicked(r.get())).pack()
Radiobutton(root, text='opcion2', variable=r, value=2, command=lambda:clicked(r.get())).pack()

def clicked(value):
    # mylabel = Label(root, text=value)
    # mylabel.pack()
    mylabel.config(text=value)


root.mainloop()

#NOTA: con este ejemplo se demuestra que si es posible aplicar cambios instantaneos en una lista
# radiobutton, sin necesidad de estar presionando un boton para que se aplique el cambio.
# en el siguiente ejemplo se hara con un boton
