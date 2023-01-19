from tkinter import *

py_root =Tk()
py_root.geometry("655x333")

def hello():
    print("Hello tkinter Buttons-pycharm")

def name():
    print("The name is neer")

frame = Frame(py_root, borderwidth=6, bg="blue", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Hello!!", command=hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="Tell me name now", command=name)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="red", text="Print now")
b3.pack(side=LEFT, padx=23)

py_root.mainloop()