from tkinter import *
from PIL import ImageTk, Image
import mysql.connector


root = Tk()
root.title('Create a CRM database tool') #CRM = Customer Relationship Management
root.geometry('400x800')

# Connect to MySQL
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='codemy'
    )
# Check to see if connection to MySQL was created
#print(mydb)

# create a cursor and initialize it
# my_cursor = mydb.cursor()

# Create a database
# my_cursor.execute('CREATE DATABASE codemy')

# Test to see if database was created
# my_cursor.execute('SHOW DATABASES')
# for db in my_cursor:
#     print(db)

# Drop table
# my_cursor.execute('DROP TABLE customers')
# mydb.commit()

# Create a table
# my_cursor.execute('''CREATE TABLE customers (
#                 first_name VARCHAR(255),
#                 last_name VARCHAR(255),
#                 zipcode INT(10),
#                 price_paid DECIMAL(10, 2),
#                 user_id INT AUTO_INCREMENT PRIMARY KEY)''')

# Alter table
# my_cursor.execute(''' ALTER TABLE customers ADD (
#                     email VARCHAR(255),
#                     address_1 VARCHAR(255),
#                     address_2 VARCHAR(255),
#                     city VARCHAR(255),
#                     state VARCHAR(255),
#                     country VARCHAR(255),
#                     phone VARCHAR(255),
#                     payment_method VARCHAR(50),
#                     discount_code VARCHAR(255)
#                     )''')

# my_cursor.execute('SELECT * FROM customers')
# # print(my_cursor.description)

# for thing in my_cursor.description:
#     print(thing)

def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

def add_customer():
    sql_command = 'INSERT INTO customers (first_name, last_name, address_1, address_2, city, state, zipcode, country, phone, email, payment_method, discount_code, price_paid) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    values = (first_name_box.get(), last_name_box.get(), address1_box.get(), address2_box.get(), city_box.get(), state_box.get(), zipcode_box.get(), country_box.get(), phone_box.get(), email_box.get(), payment_method_box.get(), discount_code_box.get(), price_paid_box.get())
    my_cursor = mydb.cursor()
    my_cursor.execute(sql_command, values)
    mydb.commit()
    clear_fields()




#Create a Label
title_label = Label(root, text='Codemy Customer Database', font=('Helvetica', 16))
title_label.grid(column=0, row=0, columnspan=2, pady=10)

# Create Main Form To Enter Customer Data
first_name_label = Label(root, text='First Name').grid(column=0, row=1, sticky=W, padx=10)
last_name_label = Label(root, text='Last Name').grid(column=0, row=2, sticky=W, padx=10)
address1_label = Label(root, text='Address 1').grid(column=0, row=3, sticky=W, padx=10)
address2_label = Label(root, text='Address 2').grid(column=0, row=4, sticky=W, padx=10)
city_label = Label(root, text='City').grid(column=0, row=5, sticky=W, padx=10)
state_label = Label(root, text='State').grid(column=0, row=6, sticky=W, padx=10)
zipcode_label = Label(root, text='Zipcode').grid(column=0, row=7, sticky=W, padx=10)
country_label = Label(root, text='Country').grid(column=0, row=8, sticky=W, padx=10)
phone_label = Label(root, text='Phone Number').grid(column=0, row=9, sticky=W, padx=10)
email_label = Label(root, text='Email Address').grid(column=0, row=10, sticky=W, padx=10)
payment_method_label = Label(root, text='Payment Method').grid(column=0, row=11, sticky=W, padx=10)
discount_code_label = Label(root, text='Discount Code').grid(column=0, row=12, sticky=W, padx=10)
price_paid_label = Label(root, text='Price Paid').grid(column=0, row=13, sticky=W, padx=10)

first_name_box = Entry(root)
first_name_box.grid(column=1, row=1, padx=10, pady=10)
last_name_box = Entry(root)
last_name_box.grid(column=1, row=2, padx=10, pady=10)
address1_box = Entry(root)
address1_box.grid(column=1, row=3, padx=10, pady=10)
address2_box = Entry(root)
address2_box.grid(column=1, row=4, padx=10, pady=10)
city_box = Entry(root)
city_box.grid(column=1, row=5, padx=10, pady=10)
state_box = Entry(root)
state_box.grid(column=1, row=6, padx=10, pady=10)
zipcode_box = Entry(root)
zipcode_box.grid(column=1, row=7, padx=10, pady=10)
country_box = Entry(root)
country_box.grid(column=1, row=8, padx=10, pady=10)
phone_box = Entry(root)
phone_box.grid(column=1, row=9, padx=10, pady=10)
email_box = Entry(root)
email_box.grid(column=1, row=10, padx=10, pady=10)
payment_method_box = Entry(root)
payment_method_box.grid(column=1, row=11, padx=10, pady=10)
discount_code_box = Entry(root)
discount_code_box.grid(column=1, row=12, padx=10, pady=10)
price_paid_box = Entry(root)
price_paid_box.grid(column=1, row=13, padx=10, pady=10)

# Create Buttons
add_customer_button = Button(root, text='Add Customer To Database', command=add_customer)
add_customer_button.grid(column=0, row=15, padx=10, pady=10)

clear_fields_button = Button(root, text='Clear Fields', command=clear_fields)
clear_fields_button.grid(column=1, row=15, padx=10, pady=10)


my_cursor = mydb.cursor()
my_cursor.execute('SELECT * FROM customers')
result = my_cursor.fetchall()
for x in result:
    print(x)









root.mainloop()
