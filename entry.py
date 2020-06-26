# tkinter is a two step thing...
# first you create a thing...
# then you put it on the screen...
# but you don't always have to...

from tkinter import *

root = Tk()

e = Entry(root, width=100, font=("Helvetica", 32))
e.pack(pady=20)
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

my_button = Button(root, text="Enter Your Name", command=myClick)
my_button.pack()

root.mainloop()
