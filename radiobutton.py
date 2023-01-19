from tkinter import *
import tkinter.messagebox as tmsg

py_root=Tk()
py_root.title("Radio button")
py_root.geometry("444x555")

def ticket():
    tmsg.showinfo("tickets are booked",f"you choose {var.get()}.Thank you !!!!")

var=StringVar()
var.set("Radio")
Label(py_root,text="Which movie do you like to see?..",font="lucida 19 bold",justify=LEFT,padx=20).pack()
radio=Radiobutton(py_root,text="Kantara",padx=15,variable=var,value="Kantara").pack(anchor="w")
radio = Radiobutton(py_root, text="Pathan", padx=15, variable=var, value="pathan").pack(anchor="w")
radio = Radiobutton(py_root, text="varisu", padx=15, variable=var, value="varisu").pack(anchor="w")

Button(text="book tickets",command=ticket).pack()
py_root.mainloop()