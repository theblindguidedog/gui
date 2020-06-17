from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Frames')

# padx & pady inside of frame
#frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
# Below... without text... looks cleaner
frame = LabelFrame(root, padx=50, pady=50)

# padx & pady outside of frame
frame.pack(padx=10, pady=10)

# You can normally only use either pack() or grid() not both.
# But with frames you can use both.
b = Button(frame, text="Don't click Here!")
b2 = Button(frame, text="OR HERE!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)



root.mainloop()
