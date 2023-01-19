from tkinter import *

py_root = Tk()

def getvals():
    print("Submitting form........")
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")

    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")

py_root.geometry("644x344")
#Heading
Label(py_root, text="Welcome to Travels GUI", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
name = Label(py_root, text="Name")
phone = Label(py_root, text="Phone")
gender = Label(py_root, text="Gender")
emergency = Label(py_root, text="Emergency Contact")
paymentmode = Label(py_root, text="Payment Mode")

#Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


#Entries for our form
nameentry = Entry(py_root, textvariable=namevalue)
phoneentry = Entry(py_root, textvariable=phonevalue)
genderentry = Entry(py_root, textvariable=gendervalue)
emergencyentry = Entry(py_root, textvariable=emergencyvalue)
paymentmodeentry = Entry(py_root, textvariable=paymentmodevalue)

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

#Checkbox & Packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Submit to Travels GUI", command=getvals).grid(row=7, column=3)

py_root.mainloop()
