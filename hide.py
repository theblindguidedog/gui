from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Entry 2")
root.geometry("400x400")
root.iconbitmap('/Users/theblindguidedog/gui/images/codemy.png')

# Create clicked function
def clicked():
	global my_label2
	input = e.get()
	my_label2 = Label(root, text="Hello " + input)
	my_label2.pack()

# Add images
#my_image = ImageTk.PhotoImage(Image.open("../gui/images/codemy.png"))
#image_label = Label(image=my_image).pack()

def hide():
	my_label2.pack_forget()
	#my_label2.destroy()

def show():
	my_label2.pack()

# Create my_label
my_label = Label(root, text="Enter Your Name:")
my_label.pack()

e = Entry(root, font=("Helvetica", 18))
e.pack(pady=20)

my_button = Button(root, text="Click Me!", command=clicked)
my_button.pack(pady=20)

hide_button = Button(root, text="Hide", command=hide)
hide_button.pack(pady=20)

show_button = Button(root, text="Show", command=show)
show_button.pack(pady=20)



root.mainloop()
