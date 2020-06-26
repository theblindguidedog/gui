# tkinter is a two step thing...
# first you create a thing...
# then you put it on the screen...
# but you don't always have to...

from tkinter import *

root = Tk()
root.title("Buttons")
root.geometry("400x400")

# Create clicked function
def clicked():
    myLabel = Label(root, text="Look! I clicked a Button!!").pack()

# Create Button Widget
myButton = Button(root, text="Click Me!", command=clicked).pack(pady=20)

root.mainloop()
