import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = self.root.title("Restaurant Management App")

        self.menu_items = {
            "FRIES MEAL": 2,
            "BURGER MEAL": 2,
            "PIZZA MEAL": 3,
            "LUNCH MEAL": 4,
            "DRINKS": 1
        }
        self.exchange_rate = 82
        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.label(
            frame,
            text="Restaurant Order Management ",
            font=("Arial", 20, "bold")
        ).grid(row=0, columspan=3, padx=10, pady=10)

        self.menu_labels = {}
        self.manu_quantities = {}

        for i, (item, price), in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item}, (${price}):"
                font=("Arial", 12)               
            )
            label.grid(row=1, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, wisth=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency: ",
            font=("Arial", 12)
        ).grid(
            row=len(self.menu_items) + 1
            column=0,
            padx=10,
            pady=5
        )
        currency_dropdown = ttk.ComboBox(
            frame, textvariable=self.currency_var,
            state="readonly"
            width=18,
            values=("USD", "INR")
        )
        currency_dropdown.grid(
            row=len(self.menu_items) + 1
            column=1,
            padx=10,
            pady=5
        )
        currency_dropdown.current(0)
        self.curreny_var.trace