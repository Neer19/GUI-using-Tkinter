from tkinter import *

def clik(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)

    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        scvalue.update()
    else:
        scvalue.set(scvalue.get()+text)
        scvalue.update()


py_root=Tk()
py_root.title("Calculator")
py_root.geometry("800x800")

py_root.wm_iconbitmap("1.ico")

scvalue=StringVar()
scvalue.set("")
screen=Entry(py_root,textvar=scvalue,font="Lucida 19 bold")
screen.pack(fill=X,ipadx=20,pady=25,padx=15)

f=Frame(py_root,bg="grey")

b=Button(f,text="9",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text="8",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text="7",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

f.pack()

f=Frame(py_root,bg="grey")

b=Button(f,text="6",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text="5",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text="4",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

f.pack()

f=Frame(py_root,bg="grey")

b=Button(f,text="3",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text="2",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text="1",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

f.pack()

f=Frame(py_root,bg="grey")

b=Button(f,text="0",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text="-",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text="*",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

f.pack()

f=Frame(py_root,bg="grey")

b=Button(f,text="/",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text="%",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text="=",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

f.pack()

f=Frame(py_root,bg="grey")

b=Button(f,text="00",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text="C",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

b=Button(f,text=".",padx=25,pady=10,font="Lucida 20 bold")
b.pack(side=LEFT,padx=20,pady=22)
b.bind("<Button-1>",clik)

f.pack()

py_root.mainloop()