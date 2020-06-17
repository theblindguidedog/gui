# tkinter is a two step thing. First you create a thing...
# then you put it on the screen.

from tkinter import *

root = Tk()
# Creating a label widget
myLabel0 = Label(root, text="Hello World!")
myLabel1 = Label(root, text="My name is Scott!")
# Shoving it onto the screen
myLabel0.grid(row=0, column=0)
myLabel1.grid(row=0, column=1)

# OR Both At The Same Time Like This: Although John Elder does it the 2 way way.

myLabel2 = Label(root, text="Shitty McGitty!").grid(row=1, column=0)
myLabel3 = Label(root, text="Turd on a wire!").grid(row=1, column=1)

root.mainloop()
