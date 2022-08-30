from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Matplotlib charts app')
root.geometry('400x400')

def graph():
    house_prices = np.random.normal(200000, 25000, 5000) #distribucion normal, 200000 es precio promedio, 25000 es la desviacion estandard, 5000 es la cantidad de datos a imprimir.
    plt.hist(house_prices, 200) #el 200 aqui es la cantidad de valores en x
    plt.show()

myButton = Button(root, text='Graph it!', command=graph)
myButton.pack()

root.mainloop()
