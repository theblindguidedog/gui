from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Root")
root.geometry("400x200")

# Create Open Dialog Box Function
def open_image():
	# Open File Dialog Box
	root.filename = filedialog.askopenfilename(
	initialdir='/Users/theblindguidedog/gui-master/images', title="Open An Image File",
	filetypes=(("GIF", "*.gif"), ("All Files", "*.*"))
	)
	my_label = Label(root, text=root.filename).pack(pady=10)



my_button = Button(root, text="Open Image", command=open_image).pack(pady=10)


root.mainloop()
