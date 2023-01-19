from tkinter import *
import tkinter.messagebox as tmsg

py_root=Tk()
py_root.title("Tkinter")
py_root.geometry("455x366")

def func():
    print("Heloo!! ......")

def help():
    print("I will help you")
    tmsg.showinfo("Help", "We will help you with this gui")

def feedback():
    print("Give feedback")
    value = tmsg.askquestion("Was your experience Good?", "You used this gui.. Was your experience Good?")
    if value == "yes":
        msg = "Great. Give the feedback on appstore please"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience", msg)

def project():
    ans = tmsg.askretrycancel("Do you like this project?", "Sorry i you do't like it")
    if ans:
        print("Retry karne pe bhi kuch nahi hoga")

    else:
        print("thank you")

# mymenu=Menu(py_root)
# mymenu.add_command(label="File",command=func)
# mymenu.add_command(label="Exit",command=quit)
# py_root.config(menu=mymenu)

mainmenu=Menu(py_root)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New",command=func)
m1.add_command(label="save",command=func)
m1.add_separator()
m1.add_command(label="save as",command=func)
m1.add_command(label="project",command=func)
py_root.config(menu=mainmenu)
mainmenu.add_cascade(label="FIle",menu=m1)

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="New",command=func)
m2.add_command(label="save",command=func)
m2.add_separator()
m2.add_command(label="save as",command=func)
m2.add_command(label="project",command=func)
py_root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="New",command=func)
m3.add_command(label="save",command=func)
m3.add_separator()
m3.add_command(label="save as",command=func)
m3.add_command(label="project",command=func)
py_root.config(menu=mainmenu)
mainmenu.add_cascade(label="View",menu=m3)

m4=Menu(mainmenu,tearoff=0)
m4.add_command(label="Help",command=help)
m4.add_command(label="feedback",command=feedback)
m4.add_command(label="project",command=project)
py_root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m4)


py_root.mainloop()