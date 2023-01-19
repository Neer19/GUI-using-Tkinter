from tkinter import *
import tkinter.messagebox as tmsg

py_root = Tk()
py_root.geometry("555x444")
py_root.title("Slider")

def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Credited!", f"We have credited {myslider2.get()} dollars to your bank account")

# myslider = Scale(py_root, from_=0, to=100)
# myslider.pack()

Label(py_root, text="How many dollars do you want?").pack()
myslider2 = Scale(py_root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
# myslider2.set(34)
myslider2.pack()

Button(py_root, text="Get dollars!", pady=10, command=getdollar).pack()

py_root.mainloop()