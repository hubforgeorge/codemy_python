from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Learn to code')
root.iconbitmap('snake.ico')

frame = LabelFrame(root, text='This is my frame', padx=50, pady=50)     #el padx y el pady en esta ubicacion me da el espaciamiento dentro del frame
frame.pack(padx=10, pady=10)                                    #el padx y el pady en esta ubicacion me da el espaciamiento afuera del frame


b = Button(frame, text='Don´t click here!')
b2 = Button(frame, text='... or here!')

b.grid(column=0, row=0)                                       #se puede usar grid aqui, pero todos tendrian que tener la misma forma de posicionamiento grid
b2.grid(column=1, row=1)



root.mainloop()
