from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("555x666")

    def status(self):
        self.var=StringVar()
        self.var.set("ready")
        self.statusbar=Label(self,textvar=self.var,relief=SUNKEN,anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)

    def clik(self):
        print("Cliked....")

    def button(self,inptext):
        Button(text=inptext,command=self.clik).pack()

if __name__=='__main__':
    window=GUI()
    window.status()
    window.button("please..clik")
    window.mainloop()
