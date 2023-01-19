from tkinter import *

py_root = Tk()
py_root.geometry("455x455")
py_root.title("Scrollbar")

# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2 scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(py_root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(py_root, yscrollcommand = scrollbar.set)
for i in range(500):
     listbox.insert(END, f"Item {i}")

listbox.pack(fill="both",padx=22)
#text = Text(root, yscrollcommand = scrollbar.set)
#text.pack(fill=BOTH)
scrollbar.config(command=listbox.yview)
#scrollbar.config(command=text.yview)

py_root.mainloop()
