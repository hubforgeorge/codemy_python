from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Checkboxes')
root.iconbitmap('snake.ico')
root.geometry('400x400')

var = StringVar()       #se puede utilizar IntVar

c = Checkbutton(root, text='Would you like to SuperSize your order? Check here!', variable=var, onvalue='SuperSize', offvalue='NormalSize')    #si se utiliza IntVar, es posible no utilizar onvalue y offvalue **revisar
c.deselect()        #utilizar obligatoriamente para inicializar el valor del stringvar, esto no ocurre con IntVar
c.pack()

def show():

    my_label = Label(root, text=var.get()).pack()

btn = Button(root, text='Select', command=show).pack()

root.mainloop()
