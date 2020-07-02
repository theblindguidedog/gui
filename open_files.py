from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Root")
root.geometry("500x700")

# Create Open Dialog Box Function
def open_image():
	# Open File Dialog Box
	root.filename = filedialog.askopenfilename(
	initialdir='/gui', title="Open An Image File",
	filetypes=(("GIF", "*.gif"), ("All Files", "*.*"))
	)
	#my_label = Label(root, text=root.filename).pack(pady=10)
	global my_img
	# Open image and place on screen
	my_img = ImageTk.PhotoImage(Image.open(root.filename))
	img_label = Label(root, image=my_img)
	img_label.pack(pady=10)



my_button = Button(root, text="Open Image", command=open_image).pack(pady=10)


root.mainloop()
