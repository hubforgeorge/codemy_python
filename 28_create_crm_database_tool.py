from tkinter import *
from PIL import ImageTk, Image
import mysql.connector


root = Tk()
root.title('Create a CRM database tool') #CRM = Customer Relationship Management
root.geometry('400x400')

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=''
    )
print(mydb)

root.mainloop()
