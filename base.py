from tkinter import *
from PIL import ImageTk,Image

# You don't want to run 2 versions of Tk()
# that's why the other is called Toplevel()
root = Tk()
root.title('Base')

def open():
    global my_img
    top = Toplevel()
    top.title('Top')
    # my_img had to be made global or python ignores and garbage collects it.
    # it doesn't need the global if it's outside the function.
    my_img = ImageTk.PhotoImage(Image.open("images/img-2.jpg"))
    my_label = Label(top,image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Image", command=open).pack()


mainloop()
