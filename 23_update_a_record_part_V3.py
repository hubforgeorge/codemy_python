import tkinter as tk
import sqlite3

class AppVentana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Actualizar un registro')

        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.direccion = tk.StringVar()
        self.ciudad = tk.StringVar()
        self.provincia = tk.StringVar()
        self.postal = tk.StringVar()
        self.id = tk.StringVar()

        self.lbl_nombre = tk.Label(self.ventana, text='Nombre: ')
        self.lbl_nombre.grid(column=0, row=0)
        self.ent_nombre = tk.Entry(self.ventana, textvariable=self.nombre)
        self.ent_nombre.grid(column=1, row=0)

        self.lbl_apellido = tk.Label(self.ventana, text='Apellido: ')
        self.lbl_apellido.grid(column=0, row=1)
        self.ent_apellido = tk.Entry(self.ventana, textvariable=self.apellido)
        self.ent_apellido.grid(column=1, row=1)

        self.lbl_direccion = tk.Label(self.ventana, text='Direccion: ')
        self.lbl_direccion.grid(column=0, row=2)
        self.ent_direccion = tk.Entry(self.ventana, textvariable=self.direccion)
        self.ent_direccion.grid(column=1, row=2)

        self.lbl_ciudad = tk.Label(self.ventana, text='Ciudad: ')
        self.lbl_ciudad.grid(column=0, row=3)
        self.ent_ciudad = tk.Entry(self.ventana, textvariable=self.ciudad)
        self.ent_ciudad.grid(column=1, row=3)

        self.lbl_provincia = tk.Label(self.ventana, text='Provincia: ')
        self.lbl_provincia.grid(column=0, row=4)
        self.ent_provincia = tk.Entry(self.ventana, textvariable=self.provincia)
        self.ent_provincia.grid(column=1, row=4)

        self.lbl_postal = tk.Label(self.ventana, text='Postal: ')
        self.lbl_postal.grid(column=0, row=5)
        self.ent_postal = tk.Entry(self.ventana, textvariable=self.postal)
        self.ent_postal.grid(column=1, row=5)

        self.btn_ingresar_registro = tk.Button(self.ventana, text='Ingresar Registro', command=self.ingresar)
        self.btn_ingresar_registro.grid(column=0, row=6, columnspan=2, padx=10, pady=10, ipadx=100)

        self.btn_mostrar_registros = tk.Button(self.ventana, text='Mostrar Registros', command=self.mostrar)
        self.btn_mostrar_registros.grid(column=0, row=7, columnspan=2, padx=10, pady=10, ipadx=100)

        self.lbl_id = tk.Label(self.ventana, text='Numero Id: ')
        self.lbl_id.grid(column=0, row=8)
        self.ent_id = tk.Entry(self.ventana, textvariable=self.id)
        self.ent_id.grid(column=1, row=8)

        self.btn_borrar_registro = tk.Button(self.ventana, text='Borrar Registro', command=self.borrar)
        self.btn_borrar_registro.grid(column=0, row=9, columnspan=2, padx=10, pady=10, ipadx=100)

        self.btn_actualizar_registro = tk.Button(self.ventana, text='Actualizar Registro', command=self.actualizar)
        self.btn_actualizar_registro.grid(column=0, row=10, columnspan=2, padx=10, pady=10, ipadx=100)



        self.ventana.mainloop()

    def ingresar(self):
        connexion = sqlite3.connect('address_book.db')
        cursor = connexion.cursor()
        sql = 'INSERT INTO addresses VALUES(?,?,?,?,?,?)'
        datos=(self.nombre.get(), self.apellido.get(), self.direccion.get(), self.ciudad.get(), self.provincia.get(), self.postal.get())
        cursor.execute(sql,datos)
        connexion.commit()
        connexion.close()

        self.nombre.set('')
        self.apellido.set('')
        self.direccion.set('')
        self.ciudad.set('')
        self.provincia.set('')
        self.postal.set('')

    def mostrar(self):
        connexion = sqlite3.connect('address_book.db')
        cursor = connexion.cursor()
        sql = 'SELECT *, oid FROM addresses'
        cursor.execute(sql)
        lista = cursor.fetchall()
        connexion.close()
        todos = ''
        for elemento in lista:
            cadena = elemento[0] + '\t' + elemento[1] + '\t' + elemento[2] + '\t' + elemento[3] + '\t' + elemento[4] + '\t' + str(elemento[5]) + '\t' +str(elemento[6]) + '\n'
            # cadena = elemento[0] + '\t' + elemento[1] + '\t' +str(elemento[6]) + '\n'
            todos = todos + cadena
        lbl_mostrar_valores = tk.Label(self.ventana, text=todos)
        lbl_mostrar_valores.grid(column=0, row=11, columnspan=2, padx=10, pady=10, ipadx=100)

    def borrar(self):
        connexion = sqlite3.connect('address_book.db')
        cursor = connexion.cursor()
        sql = 'DELETE FROM addresses WHERE oid=?'
        dato = (self.id.get(),)
        cursor.execute(sql, dato)
        connexion.commit()
        connexion.close()
        self.id.set('')

    def actualizar(self):
        self.ventana2 = tk.Tk()

        self.nombre2 = tk.StringVar()
        self.apellido2 = tk.StringVar()
        self.direccion2 = tk.StringVar()
        self.ciudad2 = tk.StringVar()
        self.provincia2 = tk.StringVar()
        self.postal2 = tk.StringVar()

        dato = (self.id.get(),)
        connexion = sqlite3.connect('address_book.db')
        cursor = connexion.cursor()
        sql = 'SELECT * FROM addresses WHERE oid=?'
        cursor.execute(sql, dato)
        lista = cursor.fetchall()
        connexion.close()

        # self.nombre2.set(lista[0][0])
        # self.apellido2.set(lista[0][1])
        # self.direccion2.set(lista[0][2])
        # self.ciudad2.set(lista[0][3])
        # self.provincia2.set(lista[0][4])
        # self.postal2.set(lista[0][5])

        self.lbl_nombre2 = tk.Label(self.ventana2, text='Nombre: ')
        self.lbl_nombre2.grid(column=0, row=0)
        self.ent_nombre2 = tk.Entry(self.ventana2, textvariable=self.nombre2)
        self.ent_nombre2.grid(column=1, row=0)

        self.lbl_apellido2 = tk.Label(self.ventana2, text='Apellido: ')
        self.lbl_apellido2.grid(column=0, row=1)
        self.ent_apellido2 = tk.Entry(self.ventana2, textvariable=self.apellido2)
        self.ent_apellido2.grid(column=1, row=1)

        self.lbl_direccion2 = tk.Label(self.ventana2, text='Direccion: ')
        self.lbl_direccion2.grid(column=0, row=2)
        self.ent_direccion2 = tk.Entry(self.ventana2, textvariable=self.direccion2)
        self.ent_direccion2.grid(column=1, row=2)

        self.lbl_ciudad2 = tk.Label(self.ventana2, text='Ciudad: ')
        self.lbl_ciudad2.grid(column=0, row=3)
        self.ent_ciudad2 = tk.Entry(self.ventana2, textvariable=self.ciudad2)
        self.ent_ciudad2.grid(column=1, row=3)

        self.lbl_provincia2 = tk.Label(self.ventana2, text='Provincia: ')
        self.lbl_provincia2.grid(column=0, row=4)
        self.ent_provincia2 = tk.Entry(self.ventana2, textvariable=self.provincia2)
        self.ent_provincia2.grid(column=1, row=4)

        self.lbl_postal2 = tk.Label(self.ventana2, text='Postal: ')
        self.lbl_postal2.grid(column=0, row=5)
        self.ent_postal2 = tk.Entry(self.ventana2, textvariable=self.postal2)
        self.ent_postal2.grid(column=1, row=5)

        self.ent_nombre2.insert(0,lista[0][0])
        self.ent_apellido2.insert(0,lista[0][1])
        self.ent_direccion2.insert(0,lista[0][2])
        self.ent_ciudad2.insert(0,lista[0][3])
        self.ent_provincia2.insert(0,lista[0][4])
        self.ent_postal2.insert(0,lista[0][5])

        self.btn_ejecutar = tk.Button(self.ventana2, text='Cambiar', command=self.ejecutar)
        self.btn_ejecutar.grid(column=1, row=6)

    def ejecutar(self):
        datos = (self.ent_nombre2.get(), self.ent_apellido2.get(), self.ent_direccion2.get(), self.ent_ciudad2.get(), self.ent_provincia.get(), self.ent_postal2.get(), self.id.get())
        print(datos)
        connexion = sqlite3.connect('address_book.db')
        cursor = connexion.cursor()
        sql = 'UPDATE addresses SET first_name=?, last_name=?, address=?, city=?, state=?, zipcode=? WHERE oid=?'
        cursor.execute(sql, datos)
        connexion.commit()
        connexion.close()
        self.ventana2.destroy()

ventana1 = AppVentana()
