from tkinter import *
py_root = Tk()
py_root.geometry("744x133")
py_root.title("GUI")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE


title_label = Label(text ='''
In word processing and desktop publishing, a hard return or paragraph break indicates a new paragraph, to be distinguished from the soft return at the end of a line internal to a paragraph.\nThis distinction allows word wrap to automatically re-flow text as it is edited, without losing paragraph breaks. \nThe software may apply vertical white space or indenting at paragraph breaks, depending on the selected style.
\nHow such documents are actually stored depends on the file format. 
\nIn plaintext files, there are two common formats.\nA line break that is inserted manually, and preserved when re-flowing, may still be distinct from a paragraph break, although this is typically not done in prose. \nHTML's <br /> tag produces a line break without ending the paragraph; the W3C recommends using it only to separate lines of verse (where each "paragraph" is a stanza), or in a street address''', bg ="red", fg="white", padx=113, pady=914, font="comicsansms 9 bold", borderwidth=5, relief=SUNKEN)


# Important Pack options
# anchor = nw(north-west)
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)


py_root.mainloop()


