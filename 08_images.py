from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Learn to code')
root.iconbitmap('snake.ico')


my_image = ImageTk.PhotoImage(Image.open('meritocracia.jpg'))
my_label = Label(root, image=my_image)
my_label.pack()


botton_quit = Button(root, text='Exit program', command=root.quit)
botton_quit.pack()


root.mainloop()
