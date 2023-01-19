from tkinter import *

def python(event):
    print(f"clik on {event.x},{event.y}")
    
py_root=Tk()
py_root.title("Event handling")
py_root.geometry("666x444")

widget=Button(py_root,text='clik the button')
widget.pack()

widget.bind('<Button-1>', python)
widget.bind('<Double-1>', quit)


py_root.mainloop()