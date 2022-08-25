from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('aprender a mostrar un icono e imagenes en python')
root.iconbitmap('snake.ico')

#para insertar imágenes en python - tkinter, se siguen 3 pasos:
#Paso1: abrir el archivo
my_image = ImageTk.PhotoImage(Image.open('meritocracia.jpg'))
#Paso2: ponerlo en un objeto python
label = Label(image=my_image)
#Paso3: ubicarlo en la pantalla
label.pack()

button = Button(root, text='Exit Program', command=root.quit)
button.pack()

root.mainloop()
