from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Forget")
root.geometry("400x400")

hello_label = Label(root)

# Submit Function
def submit():
	global hello_label
	clear()
	hello_label = Label(root, text="Hello " + e.get())
	hello_label.grid(row=3, column=0)


# Clear Function
def clear():
	hello_label.grid_forget()
	#hello_label.destroy()


# Forget
my_label = Label(root, text="Enter Your Name:").grid(row=0, column=0)

e = Entry(root)
e.grid(row=1, column=0)

my_button = Button(root, text="Submit", command=submit).grid(row=2, column=0)

clear_button = Button(root, text="Clear", command=clear).grid(row=2, column=1)



root.mainloop()
