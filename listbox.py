from tkinter import *

def add():
    global i
    lst.insert(ACTIVE,f"{i}")
    i+=1

i=0
py_root=Tk()
py_root.title("List box")
py_root.geometry("444x444")

lst = Listbox(py_root)
lst.pack()
lst.insert(END,"First item of your list box")

Button(py_root,text="Add item",command=add).pack()

py_root.mainloop()

