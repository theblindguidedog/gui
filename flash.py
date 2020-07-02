from tkinter import *
from tkinter import colorchooser
from random import randint
from math import *

root = Tk()
root.title("Flashcard App!")
root.geometry("400x400")

# How to get the cursor in the text box
# your_entry_box.focus()

# Create a function to determine add answer correct?
def add_correct(num1, num2):
	# Calculate the actual answer
	correct = num1 + num2

	# Correct and Incorrect Answer
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct " + str(num1) + " + "  + str(num2) + " = " + str(correct))
	output_answer_incorrect.set("Incorrect " + str(num1) + " + "  + str(num2) + " = " + str(correct) + " not " + add_answer.get())


	if int(add_answer.get()) == correct:
		add_correct_label.config(text=output_answer_correct.get())
	else:
		add_correct_label.config(text=output_answer_incorrect.get())


	# Clear the answer box
	add_answer.delete(0,'end')

	# Generate two more random numbers
	num_1.set(randint(0,50))
	num_2.set(randint(0,50))
	add_flash.config(text=str(num_1.get()) + " + " + str(num_2.get()), font=("Helvetica", 52))


# Create Addition Function
def add():
	hide_menu_frames()
	add_frame.pack(fill="both", expand=1)
	# Create Two Random Numbers
	global num_1, num_2
	num_1 = IntVar()
	num_2 = IntVar()
	num_1.set(randint(0,50))
	num_2.set(randint(0,50))

	# Put our random numbers onto the screen
	global add_flash
	add_flash = Label(add_frame, text=str(num_1.get()) + " + " + str(num_2.get()), font=("Helvetica", 52))
	add_flash.pack(pady=10)

	# Answer Box
	global add_answer
	add_answer = Entry(add_frame)
	add_answer.pack(pady=5)
	add_answer.focus()

	add_button = Button(add_frame, text="Answer", command=lambda: add_correct(num_1.get(), num_2.get()))
	add_button.pack(pady=5)

	# Correct or Incorrect Message
	global add_correct_label
	add_correct_label = Label(add_frame, text="")
	add_correct_label.pack(pady=5)


# Create a function to determine subtract answer correct?
def subtract_correct(num1, num2):
	# Calculate the actual answer
	correct = num1 - num2

	# Correct and Incorrect Answer
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct " + str(num1) + " - "  + str(num2) + " = " + str(correct))
	output_answer_incorrect.set("Incorrect " + str(num1) + " - "  + str(num2) + " = " + str(correct) + " not " + subtract_answer.get())


	if int(subtract_answer.get()) == correct:
		subtract_correct_label.config(text=output_answer_correct.get())
	else:
		subtract_correct_label.config(text=output_answer_incorrect.get())


	# Clear the answer box
	subtract_answer.delete(0,'end')

	# Generate two more random numbers
	num_1.set(randint(0,50))
	num_2.set(randint(0,50))
	subtract_flash.config(text=str(num_1.get()) + " - " + str(num_2.get()), font=("Helvetica", 52))


# Create Subtract Function
def subtract():
	hide_menu_frames()
	subtract_frame.pack(fill="both", expand=1)
	# Create Two Random Numbers
	global num_1, num_2
	num_1 = IntVar()
	num_2 = IntVar()
	num_1.set(randint(0,50))
	num_2.set(randint(0,50))

	# Put our random numbers onto the screen
	global subtract_flash
	subtract_flash = Label(subtract_frame, text=str(num_1.get()) + " - " + str(num_2.get()), font=("Helvetica", 52))
	subtract_flash.pack(pady=10)

	# Answer Box
	global subtract_answer
	subtract_answer = Entry(subtract_frame)
	subtract_answer.pack(pady=5)
	subtract_answer.focus()

	subtract_button = Button(subtract_frame, text="Answer", command=lambda: subtract_correct(num_1.get(), num_2.get()))
	subtract_button.pack(pady=5)

	# Correct or Incorrect Message
	global subtract_correct_label
	subtract_correct_label = Label(subtract_frame, text="")
	subtract_correct_label.pack(pady=5)


# Create a function to determine multiply answer correct?
def multiply_correct(num1, num2):
	# Calculate the actual answer
	correct = num1 * num2

	# Correct and Incorrect Answer
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct " + str(num1) + " x "  + str(num2) + " = " + str(correct))
	output_answer_incorrect.set("Incorrect " + str(num1) + " x "  + str(num2) + " = " + str(correct) + " not " + multiply_answer.get())


	if int(multiply_answer.get()) == correct:
		multiply_correct_label.config(text=output_answer_correct.get())
	else:
		multiply_correct_label.config(text=output_answer_incorrect.get())


	# Clear the answer box
	multiply_answer.delete(0,'end')

	# Generate two more random numbers
	num_1.set(randint(0,50))
	num_2.set(randint(0,50))
	multiply_flash.config(text=str(num_1.get()) + " x " + str(num_2.get()), font=("Helvetica", 52))



# Create Multiply Function
def multiply():
	hide_menu_frames()
	multiply_frame.pack(fill="both", expand=1)
	# Create Two Random Numbers
	global num_1, num_2
	num_1 = IntVar()
	num_2 = IntVar()
	num_1.set(randint(0,50))
	num_2.set(randint(0,50))

	# Put our random numbers onto the screen
	global multiply_flash
	multiply_flash = Label(multiply_frame, text=str(num_1.get()) + " x " + str(num_2.get()), font=("Helvetica", 52))
	multiply_flash.pack(pady=10)

	# Answer Box
	global multiply_answer
	multiply_answer = Entry(multiply_frame)
	multiply_answer.pack(pady=5)
	multiply_answer.focus()

	multiply_button = Button(multiply_frame, text="Answer", command=lambda: multiply_correct(num_1.get(), num_2.get()))
	multiply_button.pack(pady=5)

	# Correct or Incorrect Message
	global multiply_correct_label
	multiply_correct_label = Label(multiply_frame, text="")
	multiply_correct_label.pack(pady=5)


# Create a function to determine divide answer correct?
def divide_correct(num1, num2):
	# Calculate the actual answer
	correct = num1 / num2

	# Correct and Incorrect Answer
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct " + str(num1) + " / "  + str(num2) + " = " + str(correct))
	output_answer_incorrect.set("Incorrect " + str(num1) + " / "  + str(num2) + " = " + str(correct) + " not " + divide_answer.get())


	if float(divide_answer.get()) == correct:
		divide_correct_label.config(text=output_answer_correct.get())
	else:
		divide_correct_label.config(text=output_answer_incorrect.get())


	# Clear the answer box
	divide_answer.delete(0,'end')

	# Generate two more random numbers
	num_1.set(randint(0,100))
	num_2.set(randint(1,20)) # Cannot be zero (0, 50)
	divide_flash.config(text=str(num_1.get()) + " / " + str(num_2.get()), font=("Helvetica", 52))


# Create Divide Function
def divide():
	hide_menu_frames()
	divide_frame.pack(fill="both", expand=1)
	# Create Two Random Numbers
	global num_1, num_2
	num_1 = IntVar()
	num_2 = IntVar()
	num_1.set(randint(0,100))
	num_2.set(randint(1,10)) # Cannot be zero (0, 50)

	# Put our random numbers onto the screen
	global divide_flash
	divide_flash = Label(divide_frame, text=str(num_1.get()) + " / " + str(num_2.get()), font=("Helvetica", 52))
	divide_flash.pack(pady=10)

	# Answer Box
	global divide_answer
	divide_answer = Entry(divide_frame)
	divide_answer.pack(pady=5)
	divide_answer.focus()

	divide_button = Button(divide_frame, text="Answer", command=lambda: divide_correct(num_1.get(), num_2.get()))
	divide_button.pack(pady=5)

	# Correct or Incorrect Message
	global divide_correct_label
	divide_correct_label = Label(divide_frame, text="")
	divide_correct_label.pack(pady=5)



# Hide Frame Function
def hide_menu_frames():
	# Destroy the children widgets in each frame
	for widget in add_frame.winfo_children():
		widget.destroy()

	for widget in subtract_frame.winfo_children():
		widget.destroy()

	for widget in multiply_frame.winfo_children():
		widget.destroy()

	for widget in divide_frame.winfo_children():
		widget.destroy()

	for widget in start_frame.winfo_children():
		widget.destroy()

	# Hide all frames
	add_frame.pack_forget()
	subtract_frame.pack_forget()
	multiply_frame.pack_forget()
	divide_frame.pack_forget()
	start_frame.pack_forget()


# Define Main Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Start Screen
def home():
	hide_menu_frames()
	start_frame.pack(fill="both", expand=1)
	start_label = Label(start_frame, text="Welcome To Math Flashcards!", font=("Helvetica", 18)).pack(pady=40)
	# Button to flashcards
	a_button = Button(start_frame, text="Addition Flashcards", command=add).pack()
	s_button = Button(start_frame, text="Subtraction Flashcards", command=subtract).pack()
	m_button = Button(start_frame, text="Multiplication Flashcards", command=multiply).pack()
	d_button = Button(start_frame, text="Division Flashcards", command=divide).pack()


# Create menu items
math_menu = Menu(my_menu)
my_menu.add_cascade(label="MathCards", menu=math_menu)
math_menu.add_command(label="Add", command=add)
math_menu.add_command(label="Subtract", command=subtract)
math_menu.add_command(label="Multiply", command=multiply)
math_menu.add_command(label="Divide", command=divide)
math_menu.add_separator()
math_menu.add_command(label="Home", command=home)
math_menu.add_command(label="Exit", command=root.quit)

# Create Math Frame
add_frame = Frame(root, width=400, height=400)
subtract_frame = Frame(root, width=400, height=400)
multiply_frame = Frame(root, width=400, height=400)
divide_frame = Frame(root, width=400, height=400)
start_frame = Frame(root,height=400, width=400)


# Show Start Screen
home()


root.mainloop()
