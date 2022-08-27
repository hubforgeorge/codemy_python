from tkinter import *
import sqlite3

root = Tk()
root.title('building out the gui for our database')
# root.geometry('400x400')


def cambiar_datos():

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # c.execute('UPDATE addresses SET first_name=' + ent_nombre_actualizar.get()+ ', last_name=' + ent_apellido_actualizar.get() + ', address=' + ent_direccion_actualizar.get() + ', city=' + ent_ciudad_actualizar.get() + ', state=' + ent_provincia_actualizar.get() + ', zipcode_actualizar=' + ent_postal_actualizar.get() + 'WHERE oid=' + ent_id.get())


    c.execute('''UPDATE addresses SET
        first_name=:ent_nombre_actualizar,
        last_name=:ent_apellido_actualizar,
        address=:ent_direccion_actualizar,
        city=:ent_ciudad_actualizar,
        state=:ent_provincia_actualizar,
        zipcode=:ent_postal_actualizar
        WHERE oid=:ent_id''',
        {
        'ent_nombre_actualizar': ent_nombre_actualizar.get(),
        'ent_apellido_actualizar': ent_apellido_actualizar.get(),
        'ent_direccion_actualizar': ent_direccion_actualizar.get(),
        'ent_ciudad_actualizar': ent_ciudad_actualizar.get(),
        'ent_provincia_actualizar': ent_provincia_actualizar.get(),
        'ent_postal_actualizar': ent_postal_actualizar.get(),
        'ent_id': ent_id.get()
        })
    conn.commit()
    conn.close()

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
        print_records += str(record[0]) + '\t' + str(record[1]) + '\t' + str(record[6]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(column=0, row=11, columnspan=2)
    conn.close()

def borrar():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('DELETE FROM addresses WHERE oid=' + ent_id.get())
    conn.commit()
    conn.close()

def actualizar():
    global ent_nombre_actualizar
    global ent_apellido_actualizar
    global ent_direccion_actualizar
    global ent_ciudad_actualizar
    global ent_provincia_actualizar
    global ent_postal_actualizar

    ventana = Tk()
    ventana.title('Actualizar Datos')

    ent_nombre_actualizar = Entry(ventana, width=50 )
    ent_nombre_actualizar.grid(column=1, row=0, padx=10, pady=(10,0))

    ent_apellido_actualizar = Entry(ventana, width=50 )
    ent_apellido_actualizar.grid(column=1, row=1, padx=10)

    ent_direccion_actualizar = Entry(ventana, width=50 )
    ent_direccion_actualizar.grid(column=1, row=2, padx=10)

    ent_ciudad_actualizar = Entry(ventana, width=50 )
    ent_ciudad_actualizar.grid(column=1, row=3, padx=10)

    ent_provincia_actualizar = Entry(ventana, width=50 )
    ent_provincia_actualizar.grid(column=1, row=4, padx=10)

    ent_postal_actualizar = Entry(ventana, width=50 )
    ent_postal_actualizar.grid(column=1, row=5, padx=10)


    lbl_nombre_actualizar = Label(ventana, text='Nombre: ')
    lbl_nombre_actualizar.grid(column=0, row=0, pady=(10,0))

    lbl_apellido_actualizar = Label(ventana, text='Apellidos: ')
    lbl_apellido_actualizar.grid(column=0, row=1, padx=10)

    lbl_direccion_actualizar = Label(ventana, text='Direccion: ')
    lbl_direccion_actualizar.grid(column=0, row=2, padx=10)

    lbl_ciudad_actualizar = Label(ventana, text='Ciudad: ')
    lbl_ciudad_actualizar.grid(column=0, row=3, padx=10)

    lbl_provincia_actualizar = Label(ventana, text='Provincia: ')
    lbl_provincia_actualizar.grid(column=0, row=4, padx=10)

    lbl_postal_actualizar = Label(ventana, text='Numero Postal: ')
    lbl_postal_actualizar.grid(column=0, row=5, padx=10)

    btn_cambiar_datos = Button(ventana, text='Cambiar datos', command=cambiar_datos)
    btn_cambiar_datos.grid(column=0, row=6, columnspan=2, padx=10, pady=10, ipadx=137)

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('SELECT * FROM addresses WHERE oid=' + ent_id.get())
    dato = c.fetchall()
    conn.close()
    for elemento in dato:
        ent_nombre_actualizar.insert(0, elemento[0])
        ent_apellido_actualizar.insert(0, elemento[1])
        ent_direccion_actualizar.insert(0, elemento[2])
        ent_ciudad_actualizar.insert(0, elemento[3])
        ent_provincia_actualizar.insert(0, elemento[4])
        ent_postal_actualizar.insert(0, elemento[5])

    ventana.mainloop()





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

btn_actualizar = Button(root, text='Actualizar Registro', command=actualizar)
btn_actualizar.grid(column=0, row=10, columnspan=2, padx=10, pady=10, ipadx=137)




root.mainloop()
