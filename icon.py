from tkinter import *

py_root=Tk()
py_root.geometry("500x300")
py_root.title("GUI tkinter")
py_root.wm_iconbitmap("1.ico")

width=py_root.winfo_screenwidth()
height=py_root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="close",command=py_root.destroy).pack()

py_root.mainloop()