from tkinter import *
from tkinter import ttk # nicer looking widgets

root = Tk()
root.title('Check Boxes')
root.geometry("400x400")

# Create Select Function
def select():
	my_label = Label(root, text=my_combo.get()).pack(pady=10)

# Combo Boxes
options = [
"Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday"
]

my_combo = ttk.Combobox(root, value=options)
my_combo.current(0)
my_combo.pack(pady=10)

my_button = Button(root, text="Select", command=select).pack()


root.mainloop()
