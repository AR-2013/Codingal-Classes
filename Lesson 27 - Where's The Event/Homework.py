from tkinter import *

root = Tk()

def convert():
    inches = float(inches_entry.get())
    centimeters = inches * 2.54
    answer.config(text=centimeters)

inches_entry = Entry(root)
inches_entry.pack()

Button(root, text="Convert", command=convert).pack()

answer = Label(root, text="")
answer.pack()

root.mainloop()