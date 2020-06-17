from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("title")
root.geometry("400x200")

def graph():
    #house-price 200000, standard deviation 25000, datapoints 5000
    house_prices = np.random.normal(200000, 25000, 5000)
    # Histogram 50 bins
    #plt.hist(house_prices, 50)
    # Go to the MatLab (matplotlib) Website For More
    plt.polar(house_prices)
    plt.show()

my_button = Button(root, text="Graph It!", command=graph)
my_button.pack()




root.mainloop()
