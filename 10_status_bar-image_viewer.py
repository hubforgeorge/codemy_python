from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Learn to code')
root.iconbitmap('snake.ico')


my_img1 = ImageTk.PhotoImage(Image.open('imagenes/mano.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('imagenes/mariposa.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('imagenes/marrano.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('imagenes/mazorca.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('imagenes/pez.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('imagenes/pipa.jpg'))
my_img7 = ImageTk.PhotoImage(Image.open('imagenes/molino.jpg'))
my_img8 = ImageTk.PhotoImage(Image.open('imagenes/momia.jpg'))
my_img9 = ImageTk.PhotoImage(Image.open('imagenes/monedero.jpg'))
my_img10 = ImageTk.PhotoImage(Image.open('imagenes/mula.jpg'))
my_img11 = ImageTk.PhotoImage(Image.open('imagenes/pelota.jpg'))
my_img12 = ImageTk.PhotoImage(Image.open('imagenes/pera.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10, my_img11, my_img12]

status = Label(root, text='image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(root, image=my_img1)
my_label.grid(column=0, row=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()  #el metodo grid_forget() elimina el grid del widget, por ello el widget desaparece
    my_label = Label(root, image=image_list[image_number-1])

    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))     #se llama de forma recursiva.
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == len(image_list):
        button_forward = Button(root, text='>>', state=DISABLED)

    my_label.grid(column=0, row=0, columnspan=3)
    button_back.grid(column=0, row=1)
    button_forward.grid(column=2, row=1)

    status = Label(root, text='image ' + str(image_number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(column=0, row=2, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()  #el metodo grid_forget() elimina el grid del widget, por ello el widget desaparece
    my_label = Label(root, image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    my_label.grid(column=0, row=0, columnspan=3)
    button_back.grid(column=0, row=1)
    button_forward.grid(column=2, row=1)

    status = Label(root, text='image ' + str(image_number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(column=0, row=2, columnspan=3, sticky=W+E)

button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='Exit program', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))    #se le da al boton un valor inicial, luego back y forward se llamaran recursivamente

button_back.grid(column=0, row=1)
button_exit.grid(column=1, row=1)
button_forward.grid(column=2, row=1, pady=10)
status.grid(column=0, row=2, columnspan=3, sticky=W+E)


root.mainloop()
