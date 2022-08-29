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

        self.frm_principal = tk.Frame(self.ventana)
        self.frm_principal.grid(column=0, row=0, padx=10, pady=10)

        self.lbl_nombre = tk.Label(self.frm_principal, text='Nombre: ')
        self.lbl_nombre.grid(column=0, row=0)
        self.ent_nombre = tk.Entry(self.frm_principal, textvariable=self.nombre, width=60)
        self.ent_nombre.grid(column=1, row=0)

        self.lbl_apellido = tk.Label(self.frm_principal, text='Apellido: ')
        self.lbl_apellido.grid(column=0, row=1)
        self.ent_apellido = tk.Entry(self.frm_principal, textvariable=self.apellido, width=60)
        self.ent_apellido.grid(column=1, row=1)

        self.lbl_direccion = tk.Label(self.frm_principal, text='Direccion: ')
        self.lbl_direccion.grid(column=0, row=2)
        self.ent_direccion = tk.Entry(self.frm_principal, textvariable=self.direccion, width=60)
        self.ent_direccion.grid(column=1, row=2)

        self.lbl_ciudad = tk.Label(self.frm_principal, text='Ciudad: ')
        self.lbl_ciudad.grid(column=0, row=3)
        self.ent_ciudad = tk.Entry(self.frm_principal, textvariable=self.ciudad, width=60)
        self.ent_ciudad.grid(column=1, row=3)

        self.lbl_provincia = tk.Label(self.frm_principal, text='Provincia: ')
        self.lbl_provincia.grid(column=0, row=4)
        self.ent_provincia = tk.Entry(self.frm_principal, textvariable=self.provincia, width=60)
        self.ent_provincia.grid(column=1, row=4)

        self.lbl_postal = tk.Label(self.frm_principal, text='Postal: ')
        self.lbl_postal.grid(column=0, row=5)
        self.ent_postal = tk.Entry(self.frm_principal, textvariable=self.postal, width=60)
        self.ent_postal.grid(column=1, row=5)

        self.btn_ingresar_registro = tk.Button(self.frm_principal, text='Ingresar Registro', command=self.ingresar)
        self.btn_ingresar_registro.grid(column=0, row=6, columnspan=2, padx=10, pady=10, ipadx=200)

        self.btn_mostrar_registros = tk.Button(self.frm_principal, text='Mostrar Registros', command=self.mostrar)
        self.btn_mostrar_registros.grid(column=0, row=7, columnspan=2, padx=10, pady=10, ipadx=200)

        self.lbl_id = tk.Label(self.frm_principal, text='Numero Id: ')
        self.lbl_id.grid(column=0, row=8)
        self.ent_id = tk.Entry(self.frm_principal, textvariable=self.id, width=60)
        self.ent_id.grid(column=1, row=8)

        self.btn_borrar_registro = tk.Button(self.frm_principal, text='Borrar Registro', command=self.borrar)
        self.btn_borrar_registro.grid(column=0, row=9, columnspan=2, padx=10, pady=10, ipadx=150)

        self.btn_actualizar_registro = tk.Button(self.frm_principal, text='Actualizar Registro', command=self.actualizar)
        self.btn_actualizar_registro.grid(column=0, row=10, columnspan=2, padx=10, pady=10, ipadx=150)

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
        lbl_mostrar_valores.grid(column=0, row=12, columnspan=2, padx=10, pady=10, ipadx=100)

    def borrar(self):
        connexion = sqlite3.connect('address_book.db')
        cursor = connexion.cursor()
        sql = 'DELETE FROM addresses WHERE oid=?'
        dato = (self.id.get(),)
        cursor.execute(sql, dato)
        connexion.commit()
        connexion.close()
        self.id.set('')

    def ejecutar(self):
        datos = (self.nombre2.get(), self.apellido2.get(), self.direccion2.get(), self.ciudad2.get(), self.provincia2.get(), self.postal2.get(), self.id.get())
        connexion = sqlite3.connect('address_book.db')
        cursor = connexion.cursor()
        sql = 'UPDATE addresses SET first_name=?, last_name=?, address=?, city=?, state=?, zipcode=? WHERE oid=?'
        cursor.execute(sql, datos)
        connexion.commit()
        connexion.close()
        self.ventana2.destroy()

    def actualizar(self):
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

        self.nombre2.set(lista[0][0])
        self.apellido2.set(lista[0][1])
        self.direccion2.set(lista[0][2])
        self.ciudad2.set(lista[0][3])
        self.provincia2.set(lista[0][4])
        self.postal2.set(lista[0][5])

        self.valores = self.nombre2.get() + self.apellido2.get() + self.direccion2.get()



        self.ventana2 = tk.Toplevel(self.ventana)
        self.ventana2.title('Segunda Ventana')
        self.lbl_valores = tk.Label(self.ventana2, text=self.valores)
        self.lbl_valores.grid(column=0, row=0)


        self.frm_secundaria = tk.Frame(self.ventana2)
        self.frm_secundaria.grid(column=0, row=1)

        self.lbl_nombre2 = tk.Label(self.frm_secundaria, text='Nombre: ')
        self.lbl_nombre2.grid(column=0, row=0)
        self.ent_nombre2 = tk.Entry(self.frm_secundaria, textvariable=self.nombre2)
        self.ent_nombre2.grid(column=1, row=0)

        self.lbl_apellido2 = tk.Label(self.frm_secundaria, text='Apellido: ')
        self.lbl_apellido2.grid(column=0, row=1)
        self.ent_apellido2 = tk.Entry(self.frm_secundaria, textvariable=self.apellido2)
        self.ent_apellido2.grid(column=1, row=1)

        self.lbl_direccion2 = tk.Label(self.frm_secundaria, text='Direccion: ')
        self.lbl_direccion2.grid(column=0, row=2)
        self.ent_direccion2 = tk.Entry(self.frm_secundaria, textvariable=self.direccion2)
        self.ent_direccion2.grid(column=1, row=2)

        self.lbl_ciudad2 = tk.Label(self.frm_secundaria, text='Ciudad: ')
        self.lbl_ciudad2.grid(column=0, row=3)
        self.ent_ciudad2 = tk.Entry(self.frm_secundaria, textvariable=self.ciudad2)
        self.ent_ciudad2.grid(column=1, row=3)

        self.lbl_provincia2 = tk.Label(self.frm_secundaria, text='Provincia: ')
        self.lbl_provincia2.grid(column=0, row=4)
        self.ent_provincia2 = tk.Entry(self.frm_secundaria, textvariable=self.provincia2)
        self.ent_provincia2.grid(column=1, row=4)

        self.lbl_postal2 = tk.Label(self.frm_secundaria, text='Postal: ')
        self.lbl_postal2.grid(column=0, row=5)
        self.ent_postal2 = tk.Entry(self.frm_secundaria, textvariable=self.postal2)
        self.ent_postal2.grid(column=1, row=5)

        print(self.nombre2.get())
        print(self.apellido2.get())
        print(self.direccion2.get())
        print(self.ciudad2.get())
        print(self.provincia2.get())
        print(self.postal2.get())

        self.btn_ejecutar = tk.Button(self.frm_secundaria, text='Cambiar', command=self.ejecutar)
        self.btn_ejecutar.grid(column=0, row=6, rowspan=2)

        self.ventana2.mainloop()


ventana1 = AppVentana()
