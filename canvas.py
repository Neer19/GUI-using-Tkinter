from tkinter import *

py_root=Tk()
can_width=800
can_height=600
py_root.geometry(f"{can_width}x{can_height}")

can_widget=Canvas(py_root,width=can_width,height=can_height)
can_widget.pack()

can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="red")
can_widget.create_oval(0,200,300,0,fill="blue")

py_root.mainloop()