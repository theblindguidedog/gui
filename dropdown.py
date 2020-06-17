from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Check')
root.geometry("400x400")

# Drop Down Boxes

def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = [
"Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday"
]

clicked = StringVar()
clicked.set(options[0])

# For some reason you need a star (*) before the list called options, kinda like pointers.
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
