from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()
root.title('Learn to code')
root.iconbitmap('snake.ico')

def popup():
    # messagebox.showinfo('This is my popup!', 'Hello World!')
    # messagebox.showwarning('This is my popup!', 'Hello World!')
    # messagebox.showerror('This is my popup!', 'Hello World!')
    # messagebox.askquestion('This is my popup!', 'Hello World!')
    # messagebox.askokcancel('This is my popup!', 'Hello World!')
    response = messagebox.askquestion('This is my popup!', 'Hello World!')
    Label(root, text=response).pack()
    if response == 'yes':
        Label(root, text='You clicked Yes').pack()
    else:
        Label(root, text='You clicked No').pack()

Button(root, text='Popup', command=popup).pack()

root.mainloop()

# askquestion retorna yes / no a pesar que en la pregunta dice si/no. el resto devuelve 1 o 0
