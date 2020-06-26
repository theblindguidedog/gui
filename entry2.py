from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Entry 2")
root.geometry("400x400")
root.iconbitmap('/Users/theblindguidedog/gui/images/codemy.png')

# Create clicked function
def clicked():
    my_label = Label(root, text="Hello " + e.get() + "!").pack()

# Add images
my_image = ImageTk.PhotoImage(Image.open("../gui/images/codemy.png"))
image_label = Label(image=my_image).pack()
# Create my_label
my_label = Label(root, text="Enter Your Name:").pack()

e = Entry(root, font=("Helvetica", 18))
e.pack(pady=20)

my_button = Button(root, text="Click Me!", command=clicked)
my_button.pack(pady=20)



root.mainloop()
