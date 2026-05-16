from tkinter import *

root = Tk()
root.title("Interest Calculator")
root.geometry("300x300")

def calculate():
    p = float(principal.get())
    r = float(rate.get())
    t = float(time.get())

    si = (p * r * t) / 100

    answer.config(text="Simple Interest = " + str(si))

Label(root, text="Principal").pack()
principal = Entry(root)
principal.pack()

Label(root, text="Rate").pack()
rate = Entry(root)
rate.pack()

Label(root, text="Time").pack()
time = Entry(root)
time.pack()

Button(root, text="Calculate", command=calculate).pack()

answer = Label(root, text="")
answer.pack()

root.mainloop()