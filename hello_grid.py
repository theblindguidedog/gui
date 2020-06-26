from tkinter import *

# Creating an Instance
root = Tk()
root.title("Hello World!")
root.geometry("400x400")

# You can also use foreground for fg or background for bg
# relief options are groove, raised, ridge, solid, sunken or flat(default)
# state can also be "disabled" or no state at all
myLabel = Label(
    root, text="Hello World!",
    font=("Helvetica", 40),
    fg="#ffffff",
    bg="#000000"
    )
# We can use sticky=W or E or N or S
# or all of them separated by commas
# We can use rowspan too
myLabel.grid(row=0, column=0, columnspan=2)

myLabel2 = Label(root, text="Second Thing!")
myLabel2.grid(row=1, column=0)

myLabel3 = Label(root, text="Third Thing!")
myLabel3.grid(row=2, column=1)




root.mainloop()
