from tkinter import *

# Creating an Instance
root = Tk()
root.title("Hello World!")
root.geometry("400x400")

# You can also use foreground for fg or background for bg
# relief options are groove, raised, ridge, solid, sunken or flat(default)
# state can also be "disabled" or no state at all
myLabel = Label(
    root, text="Hello World!",
    font=("Helvetica", 40),
    height=100,
    width=200,
    fg="#ffffff",
    bg="red",
    relief="groove",
    state="normal",
    )

myLabel.pack(pady=50)

root.mainloop()
