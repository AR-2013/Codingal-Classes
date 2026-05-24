import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    comp_label.config(text="Computer chose: " + computer_choice)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=result)

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.config(bg="lightblue")

title = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title.pack(pady=10)

instruction = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 12),
    bg="lightblue"
)
instruction.pack(pady=5)

rock_btn = tk.Button(
    root,
    text="Rock",
    width=12,
    command=lambda: play("Rock")
)
rock_btn.pack(pady=5)

paper_btn = tk.Button(
    root,
    text="Paper",
    width=12,
    command=lambda: play("Paper")
)
paper_btn.pack(pady=5)

scissors_btn = tk.Button(
    root,
    text="Scissors",
    width=12,
    command=lambda: play("Scissors")
)
scissors_btn.pack(pady=5)

comp_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="lightblue"
)
comp_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="lightblue"
)
result_label.pack(pady=10)

root.mainloop()