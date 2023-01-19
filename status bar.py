from tkinter import *

def update():
    status.set("Busy...")
    sbar.update()
    import  time
    time.sleep(2)
    status.set("Ready now....")

py_root=Tk()
py_root.title("Status bar")
py_root.geometry("344x455")

status=StringVar()
status.set("Ready")

sbar=Label(py_root,textvariable=status,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(py_root,text="upload",command=update).pack()
py_root.mainloop()