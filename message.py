from tkinter import *
from PIL import ImageTk, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Message Box')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.showerror("This is my Popup!", "Hello World!")
    #Label(root, text=response).pack()
    if response == 1 or response == "yes":
        Label(root, text="You Clicked Yes!").pack()
    elif response == "ok":
        Label(root, text="You Clicked Ok!").pack()
    else:
        Label(root, text="You Clicked No!").pack()

Button(root, text="Popup", command=popup).pack()



mainloop()
