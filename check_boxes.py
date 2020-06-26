from tkinter import *

root = Tk()
root.title('Check Boxes')
root.geometry("400x400")

def toppings():
	if v.get() == "Pepperoni":
		my_label = Label(root, text="You ordered Pepperoni")
	else:
		my_label = Label(root, text="You don't want Pepperoni")
	#my_label = Label(root, text=v.get())
	my_label.pack(pady=10)

v = StringVar()

my_check = Checkbutton(root, text="Pepperoni", variable=v, onvalue="Pepperoni", offvalue=" ")
my_check.deselect()
my_check.pack()

myButton = Button(root, text="Select Toppings", command=toppings).pack()

root.mainloop()
