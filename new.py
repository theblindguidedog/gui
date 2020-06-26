from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("New Window")
root.geometry("400x200")

# Create 2nd window function
def open_window():
	new = Toplevel()
	new.title("New Window")
	new.geometry("500x700")

	my_label = Label(new, text="Look at my fancy second window!").pack(pady=20)

	my_img = ImageTk.PhotoImage(Image.open("images/img-7.gif"))
	img_label = Label(new, image=my_img)
	img_label.pack(pady=5)

	destroy_button = Button(new, text="Quit", command=new.destroy)
	
	destroy_button.pack(pady=5)

	# Withdraw Original Window
	hide_button = Button(new, text="Hide Main Window", command=root.withdraw).pack()
	show_button = Button(new, text="Show Main Window", command=root.deiconify).pack()

	# Kill Original Window
	kill_original = Button(new, text="Quit All", command=root.destroy).pack()

	new.mainloop()

# Create New Window
open_window_button = Button(root, text="Open Image Window", command=open_window).pack()
destroy_button = Button(root, text="Quit", command=root.destroy).pack()



root.mainloop()
