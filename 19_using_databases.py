from tkinter import *
import sqlite3

root = Tk()
root.title('Using Databases')
root.geometry('400x400')

conn = sqlite3.connect('address_book.db')
c = conn.cursor()
c.execute('''CREATE TABLE addresses (
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer
                )''')

conn.commit()
conn.close()


root.mainloop()

