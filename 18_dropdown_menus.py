from tkinter import *

root = Tk()
root.title('Checkboxes')
root.geometry('400x400')

def show():
    my_label = Label(root, text=clicked.get()).pack()

options = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

clicked = StringVar()
clicked.set(options[0])

# clicked.set('Monday')
# drop = OptionMenu(root, clicked, 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text='Show selection', command=show).pack()

root.mainloop()
