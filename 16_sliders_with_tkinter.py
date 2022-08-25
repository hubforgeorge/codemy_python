from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code')
root.geometry('400x400')

vertical = Scale(root, from_=0, to=400)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))

# horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=slide)
# horizontal.pack()
my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text='Click me!', command=slide).pack()

root.mainloop()
