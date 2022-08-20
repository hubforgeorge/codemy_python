from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Learn to code')

def open():
    global my_image
    filename = filedialog.askopenfilename(initialdir='/home/jorge/Documentos/codemy_python', title='Select a file', filetypes=(('png files','*.png'),('all files','*.*')))
    my_label = Label(root, text=filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(filename))
    my_image_label = Label(root, image=my_image).pack()

btn = Button(root, text='open file', command=open).pack()

root.mainloop()
