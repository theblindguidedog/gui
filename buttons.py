# tkinter is a two step thing...
# first you create a thing...
# then you put it on the screen...
# but you don't always have to...

from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()

root.mainloop()
