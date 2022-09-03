from tkinter import *
from PIL import ImageTk, Image
import mysql.connector


root = Tk()
root.title('Create a CRM database tool') #CRM = Customer Relationship Management
root.geometry('400x400')

# Connect to MySQL
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='codemy'
    )
#Check to see if connection to MySQL was created
#print(mydb)

#create a cursor and initialize it
my_cursor = mydb.cursor()

# Create a database
# my_cursor.execute('CREATE DATABASE codemy')

# Test to see if database was created
# my_cursor.execute('SHOW DATABASES')
# for db in my_cursor:
#     print(db)

# Create a table
# my_cursor.execute('''CREATE TABLE customers (
#                 first_name VARCHAR(255),
#                 last_name VARCHAR(255),
#                 zipcode INT(10),
#                 price_paid DECIMAL(10, 2),
#                 user_id INT AUTO_INCREMENT PRIMARY KEY)''')

my_cursor.execute('SELECT * FROM customers')
# print(my_cursor.description)

for thing in my_cursor.description:
    print(thing)

root.mainloop()
