from tkinter import *
from PIL import  ImageTk, Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text

py_root = Tk()
py_root.title("CodeWithHarry News - Aapka Apna Akhabaar")
py_root.geometry("1000x1000")

texts = []
photos = []
for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")
    #TODO: Resize these images
    image = image.resize((230, 195), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(py_root, width=800, height=70)
Label(f0, text="Code With News India", font="lucida 33 bold").pack()
Label(f0, text="January 19, 2023", font="lucida 13 bold").pack()
f0.pack()


f1 = Frame(py_root, width=900, height=200, pady=14)
Label(f1, text=texts[0], padx=22, pady=22).pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")


f2 = Frame(py_root, width=900, height=200, pady=14, padx=22)
Label(f2, text=texts[1], padx=22, pady=22).pack(side="right")
Label(f2, image=photos[1], anchor="e", padx=22).pack()
f2.pack(anchor="w")


f3 = Frame(py_root, width=900, height=200, pady=34)
Label(f3, text=texts[2], padx=30, pady=22).pack(side="left")
Label(f3, image=photos[2], anchor="e").pack()
f3.pack(anchor="w")

py_root.mainloop()