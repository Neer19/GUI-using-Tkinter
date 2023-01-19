from tkinter import *

def vals():
    print("username =",uservalue.get())
    print("password=",passvalue.get())

py_root=Tk()
py_root.geometry("600x400")
py_root.title("login page")

user=Label(py_root,text="Username")
password=Label(py_root,text="password")
user.grid()
password.grid(row=1)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(py_root,textvariable=uservalue)
passentry=Entry(py_root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=vals).grid()
py_root.mainloop()