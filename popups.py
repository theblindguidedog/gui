from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Check Boxes')
root.geometry("400x400")

# Create Popup Function
def popup():
	response = messagebox.askquestion("Popup Title", "Look at my popup message!!")
	my_label = Label(root, text=response).pack(pady=10)

	"""
	if response == "yes":
		my_label = Label(root, text="You clicked Yes!").pack(pady=10)
	else:
		my_label = Label(root, text="You clicked No!").pack(pady=10)

	"""

# Popup Boxes
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

pop_button = Button(root, text="Click To Pop Up!", command=popup)
pop_button.pack(pady=20)



root.mainloop()
