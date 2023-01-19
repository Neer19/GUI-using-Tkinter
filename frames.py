from tkinter import  *

py_root=Tk()
py_root.geometry("500x400")

frame1=Frame(py_root,borderwidth=9,bg="yellow",relief=SUNKEN)
frame1.pack(side=TOP,fill="x")

frame2=Frame(py_root,borderwidth=9,bg="blue",relief=SUNKEN)
frame2.pack(side=LEFT,fill="y")

label=Label(frame1,text="Python tkinter project",font="Helvetica 20 bold",fg="red",pady=20)
label.pack()

label=Label(frame2,text="Heloo!!! welcome to the tkinter")
label.pack( pady=100)



py_root.mainloop()