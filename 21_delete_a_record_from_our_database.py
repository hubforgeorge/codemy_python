from tkinter import *
import sqlite3

root = Tk()
root.title('building out the gui for our database')
# root.geometry('400x400')

def registro():

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('INSERT INTO addresses VALUES(:ent_nombre, :ent_apellido, :ent_direccion, :ent_ciudad, :ent_provincia, :ent_postal)',
        {
        'ent_nombre': ent_nombre.get(),
        'ent_apellido': ent_apellido.get(),
        'ent_direccion': ent_direccion.get(),
        'ent_ciudad': ent_ciudad.get(),
        'ent_provincia': ent_provincia.get(),
        'ent_postal': ent_postal.get()
        })
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
    c.execute('SELECT *, oid FROM addresses')
    registros = c.fetchall()  #fetchall convierte el resultado del objeto c.execute en una lista
    # print(registros)

    print_records = ''
    for record in registros:
        print_records += str(record[0]) + ' ' + str(record[1]) + '\t' + str(record[6]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(column=0, row=10, columnspan=2)
    conn.close()

def borrar():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('DELETE FROM addresses WHERE oid=' + ent_id.get())
    conn.commit()
    conn.close()

ent_nombre = Entry(root, width=50 )
ent_nombre.grid(column=1, row=0, padx=10, pady=(10,0))

ent_apellido = Entry(root, width=50 )
ent_apellido.grid(column=1, row=1, padx=10)

ent_direccion = Entry(root, width=50 )
ent_direccion.grid(column=1, row=2, padx=10)

ent_ciudad = Entry(root, width=50 )
ent_ciudad.grid(column=1, row=3, padx=10)

ent_provincia = Entry(root, width=50 )
ent_provincia.grid(column=1, row=4, padx=10)

ent_postal = Entry(root, width=50 )
ent_postal.grid(column=1, row=5, padx=10)

ent_id = Entry(root, width=50 )
ent_id.grid(column=1, row=8, padx=10)



lbl_nombre = Label(root, text='Nombre: ')
lbl_nombre.grid(column=0, row=0, pady=(10,0))

lbl_apellido = Label(root, text='Apellidos: ')
lbl_apellido.grid(column=0, row=1, padx=10)

lbl_direccion = Label(root, text='Direccion: ')
lbl_direccion.grid(column=0, row=2, padx=10)

lbl_ciudad = Label(root, text='Ciudad: ')
lbl_ciudad.grid(column=0, row=3, padx=10)

lbl_provincia = Label(root, text='Provincia: ')
lbl_provincia.grid(column=0, row=4, padx=10)

lbl_postal = Label(root, text='Numero Postal: ')
lbl_postal.grid(column=0, row=5, padx=10)

lbl_id = Label(root, text='Numero Id: ')
lbl_id.grid(column=0, row=8, padx=10)


btn_insertar = Button(root, text='Ingresar Registro', command=registro)
btn_insertar.grid(column=0, row=6, columnspan=2, padx=10, pady=10, ipadx=137)

btn_mostrar = Button(root, text='Mostrar Registro', command=mostrar)
btn_mostrar.grid(column=0, row=7, columnspan=2, padx=10, pady=10, ipadx=137)

btn_borrar = Button(root, text='Borrar Registro', command=borrar)
btn_borrar.grid(column=0, row=9, columnspan=2, padx=10, pady=10, ipadx=137)




root.mainloop()
