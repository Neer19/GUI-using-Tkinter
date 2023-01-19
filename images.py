from tkinter import *
from PIL import Image, ImageTk

py_root = Tk()
py_root.geometry("8000x4500")
# photo = PhotoImage(file="im.png")

# for jpg
image=Image.open("im2.jpg")
photo=ImageTk.PhotoImage(image)
tkinter = Label(image=photo)
tkinter.pack()

py_root.mainloop()
