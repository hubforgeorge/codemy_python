from tkinter import *
import sqlite3

root = Tk()
root.title('building out the gui for our database')
root.geometry('400x400')

def registro():
    # nombre = ent_nombre.get()
    # apellido = ent_apellido.get()
    # direccion = ent_direccion.get()
    # ciudad = ent_ciudad.get()
    # provincia = ent_provincia.get()
    # postal = ent_postal.get()

    datos = (ent_nombre.get(), ent_apellido.get(), ent_direccion.get(), ent_ciudad.get(), ent_provincia.get(), ent_postal.get())

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    #c.execute('INSERT INTO addresses VALUES(?,?,?,?,?,?)',(nombre, apellido, direccion, ciudad, provincia, postal))
    c.execute('INSERT INTO addresses VALUES(?,?,?,?,?,?)',datos)
    conn.commit()
    conn.close()

    ent_nombre.delete(0, END)
    ent_apellido.delete(0, END)
    ent_direccion.delete(0, END)
    ent_ciudad.delete(0, END)
    ent_provincia.delete(0, END)
    ent_postal.delete(0, END)

def mostrar():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    lista = c.execute('SELECT * FROM addresses')
    fila =  8
    for elemento in lista:
        cadena = 'Nombre: '+ elemento[0] + '  Apellidos: ' + elemento[1] + '  Direccion: ' + elemento[2] + '  Ciudad: ' + elemento[3] + '  Provincia: ' + elemento[4] + '  Postal: ' + str(elemento[5])

        lbl_datos = Label(root, text=cadena)
        lbl_datos.grid(column=0, row=fila, columnspan=2)
        fila += 1
    conn.close()

ent_nombre = Entry(root, width=50 )
ent_nombre.grid(column=1, row=0)

ent_apellido = Entry(root, width=50 )
ent_apellido.grid(column=1, row=1)

ent_direccion = Entry(root, width=50 )
ent_direccion.grid(column=1, row=2)

ent_ciudad = Entry(root, width=50 )
ent_ciudad.grid(column=1, row=3)

ent_provincia = Entry(root, width=50 )
ent_provincia.grid(column=1, row=4)

ent_postal = Entry(root, width=50 )
ent_postal.grid(column=1, row=5)

lbl_nombre = Label(root, text='Nombre: ')
lbl_nombre.grid(column=0, row=0)

lbl_apellido = Label(root, text='Apellidos: ')
lbl_apellido.grid(column=0, row=1)

lbl_direccion = Label(root, text='Direccion: ')
lbl_direccion.grid(column=0, row=2)

lbl_ciudad = Label(root, text='Ciudad: ')
lbl_ciudad.grid(column=0, row=3)

lbl_provincia = Label(root, text='Provincia: ')
lbl_provincia.grid(column=0, row=4)

lbl_postal = Label(root, text='Numero Postal: ')
lbl_postal.grid(column=0, row=5)

btn_insertar = Button(root, text='Ingresar Registro', command=registro)
btn_insertar.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

btn_mostrar = Button(root, text='Mostrar Registro', command=mostrar)
btn_mostrar.grid(column=0, row=7, columnspan=2, padx=10, pady=10)




root.mainloop()
