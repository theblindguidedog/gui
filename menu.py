from tkinter import *

root = Tk()
root.title("Menu")
root.geometry("400x400")
root.iconbitmap('/Users/theblindguidedog/gui/images/codemy.png')

# Define fake command
def fake_command():
	my_label = Label(root, text="You clicked a menu item!")
	my_label.pack()

# Define a Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Menu Items
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=fake_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create another submenu Edit
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=fake_command)
edit_menu.add_command(label="Copy", command=fake_command)
edit_menu.add_command(label="Paste", command=fake_command)


root.mainloop()