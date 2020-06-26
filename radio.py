from tkinter import *

root = Tk()
root.title("Radio Buttons")

# Radio Buttons
# v = IntVar() and v.set(1) can be above or below the function
v = IntVar()
v.set(1) # sets which is checked by default 1 or 2

# Create radio button function
def radio():
	if v.get() == 1:
		my_label = Label(root, text=v.get())
	else:
		my_label = Label(root, text=v.get())
	
	my_label.pack(pady=10)



rbutton_1 = Radiobutton(root, text="One", variable=v, value=1).pack()
rbutton_2 = Radiobutton(root, text="Two", variable=v, value=2).pack()

my_button = Button(root, text="Click Me", command=radio)
my_button.pack(pady=20)



root.mainloop()