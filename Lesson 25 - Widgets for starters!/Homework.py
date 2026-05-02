from tkinter import *

root = Tk()
root.title("Homework")
root.geometry("300x300")

lbl1 = Label(text="Enter your first number", fg="white", bg="purple", height=2, width=30)
num1_entry = Entry()

lbl2 = Label(text="Enter your second number", fg="white", bg="purple", height=2, width=30)
num2_entry = Entry()

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        product = num1 * num2

        text_box.delete("1.0", END)
        text_box.insert(END, "Product: " + str(product))
    except:
        text_box.delete("1.0", END)
        text_box.insert(END, "Invalid input")

btn = Button(text="ENTER", height=1, bg="purple", fg="white", command=calculate)

text_box = Text(height=3)

lbl1.pack()
num1_entry.pack()
lbl2.pack()
num2_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()