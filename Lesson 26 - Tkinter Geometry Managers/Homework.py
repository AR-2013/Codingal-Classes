from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator")
root.geometry("350x300")

Label(root, text="Enter Day").pack()
day_entry = Entry(root)
day_entry.pack()

Label(root, text="Enter Month").pack()
month_entry = Entry(root)
month_entry.pack()

Label(root, text="Enter Year").pack()
year_entry = Entry(root)
year_entry.pack()

result_label = Label(root, text="", fg="blue")
result_label.pack(pady=10)

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = date.today()
        birth_date = date(year, month, day)

        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"You are {age} years old")

    except:
        result_label.config(text="Invalid input. Please enter valid numbers.")

Button(root, text="Calculate Age", command=calculate_age, bg="green", fg="white").pack(pady=10)

root.mainloop()