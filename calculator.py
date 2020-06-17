# tkinter is a two step thing...
# first you create a thing...
# then you put it on the screen...
# but you don't always have to...

from tkinter import *

root = Tk()

root.title("Simple Calculator")

e = Entry(root, width=15, borderwidth=10)

e.grid(row=0, column=0, columnspan=4, padx=40, pady=20)


def add_number(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    number = e.get()
    global math
    global f_num
    math = "addition"
    f_num = int(number)
    e.delete(0, END)


def button_subtract():
    number = e.get()
    global math
    global f_num
    math = "subtraction"
    f_num = int(number)
    e.delete(0, END)


def button_multiply():
    number = e.get()
    global math
    global f_num
    math = "multiplication"
    f_num = int(number)
    e.delete(0, END)


def button_divide():
    number = e.get()
    global math
    global f_num
    math = "division"
    f_num = int(number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))


# Put Buttons on the Screen

# Spacers

spacer = Button(root, text="", padx=53, pady=20)
spacer.grid(row=1, column=1, columnspan=2)

spacer_2 = Button(root, text=" ", padx=22, pady=20)
spacer_2.grid(row=5, column=2)

# Buttons

button_clear = Button(root, text="C", padx=20, pady=20, command=button_clear)
button_clear.grid(row=1, column=0)

button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: add_number(7))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: add_number(8))
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: add_number(9))

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: add_number(4))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: add_number(5))
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: add_number(6))

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: add_number(1))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: add_number(2))
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: add_number(3))

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_0 = Button(root, text="0", padx=50, pady=20, command=lambda: add_number(0))
button_0.grid(row=5, column=0, columnspan=2)

button_divide = Button(root, text="/", padx=22, pady=20, command=button_divide)
button_divide.grid(row=1, column=3)

button_multiply = Button(root, text="*", padx=21, pady=20, command=button_multiply)
button_multiply.grid(row=2, column=3)

button_subtract = Button(root, text="-", padx=21, pady=20, command=button_subtract)
button_subtract.grid(row=3, column=3)

button_add = Button(root, text="+", padx=20, pady=20, command=button_add)
button_add.grid(row=4, column=3)

button_equal = Button(root, text="=", padx=20, pady=20, command=button_equal)
button_equal.grid(row=5, column=3)

root.mainloop()
