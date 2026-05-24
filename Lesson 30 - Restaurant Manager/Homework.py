import tkinter as tk

def check_strength():
    password = password_entry.get()
    length = len(password)

    if length == 0:
        result = "Please enter a password"
    elif length < 5:
        result = "Weak Password"
    elif length < 8:
        result = "Medium Password"
    else:
        result = "Strong Password"

    result_label.config(text=result)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="lightyellow")

title = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 16, "bold"),
    bg="lightyellow"
)
title.pack(pady=10)

instruction = tk.Label(
    root,
    text="Enter your password:",
    font=("Arial", 12),
    bg="lightyellow"
)
instruction.pack(pady=5)

password_entry = tk.Entry(
    root,
    width=25,
    show="*",
    font=("Arial", 12)
)
password_entry.pack(pady=5)

check_button = tk.Button(
    root,
    text="Check Strength",
    command=check_strength,
    width=15
)
check_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="lightyellow"
)
result_label.pack(pady=10)

root.mainloop()