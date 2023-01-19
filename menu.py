from tkinter import *

py_root=Tk()
py_root.title("Tkinter")
py_root.geometry("455x366")

def func():
    print("Heloo!! ......")
# mymenu=Menu(py_root)
# mymenu.add_command(label="File",command=func)
# mymenu.add_command(label="Exit",command=quit)
# py_root.config(menu=mymenu)

mainmenu=Menu(py_root)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New",command=func)
m1.add_command(label="save",command=func)
m1.add_separator()
m1.add_command(label="save as",command=func)
m1.add_command(label="project",command=func)
py_root.config(menu=mainmenu)
mainmenu.add_cascade(label="FIle",menu=m1)

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="New",command=func)
m2.add_command(label="save",command=func)
m2.add_separator()
m2.add_command(label="save as",command=func)
m2.add_command(label="project",command=func)
py_root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="New",command=func)
m3.add_command(label="save",command=func)
m3.add_separator()
m3.add_command(label="save as",command=func)
m3.add_command(label="project",command=func)
py_root.config(menu=mainmenu)
mainmenu.add_cascade(label="View",menu=m3)


py_root.mainloop()