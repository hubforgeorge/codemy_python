from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Learn to code')
root.iconbitmap('snake.ico')

TOPPINGS = [('Pepperoni','Pepperoni'),
        ('Cheese','Cheese'),
        ('Mushroom','Mushroom'),
        ('Onion','Onion'),
        ]

pizza = StringVar()
pizza.set('Pepperoni')

for texto, topping in TOPPINGS:
    Radiobutton(root, text=texto, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()

myButton = Button(root, text='Click me!', command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()

#NOTA: con este ejemplo creamos un listado que se imprimira en la pantalla con el for,
#el resultado se mostrara luego de presionar el boton.
