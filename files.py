from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Files')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="/Users/theblindguidedog/Graphic-User-Interfaces/images",
        title="Select A File",
        filetypes=(
        ("ico files", "*.ico"),
        ("gif files", "*.gif"),
        ("png files", "*.png"),
        ("jpg files", "*.jpg"),
        ("all files", "*.*")
        )
    )
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()

# It works with just mainloop() without root(dot) for some reason.
root.mainloop()
