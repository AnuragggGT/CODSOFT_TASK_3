# IMPORT ALL THE NECESSARY MODULES

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import random,string


# Function to generate password

def gen_pass():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be positive")
        
        characters = ""
        if var_upper.get():
            characters += string.ascii_uppercase
        if var_lower.get():
            characters += string.ascii_lowercase
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation
        
        if not characters:
            msgbox.showwarning("Selection Missing", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        pass_display.config(state='normal')
        pass_display.delete(0, tk.END)
        pass_display.insert(0, password)
        pass_display.config(state='readonly')
    except ValueError:
        msgbox.showerror("Invalid Input", "Please enter a valid number for length.")

# Setup main window

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")
root.config(bg="#a0d2fd")

# Title Label

title_label = tk.Label(root, text="Secure Password Generator", font=("Helvetica", 20, "bold"),bg="#a0d2fd", fg="#333")
title_label.pack(pady=20)

# Password Length

length_frame = tk.Frame(root, bg="#91f396")
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Password Length:", font=("Helvetica", 15), bg="#91f396")
length_label.pack(side="left")

length_entry = tk.Entry(length_frame, font=("Helvetica", 15), bg="#f3db91", width=10, justify="center")
length_entry.pack(side="left", padx=10)
length_entry.insert(0, "12")

# Options for password characters
options_frame = tk.LabelFrame(root, text="Include Characters", font=("Helvetica", 15), bg="#fd95d2", fg="#333", padx=10, pady=10)
options_frame.pack(pady=10)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=var_upper, bg="#ccadc4", font=("Helvetica", 15)).pack(anchor="w")
tk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=var_lower, bg="#ccadc4", font=("Helvetica", 15)).pack(anchor="w")
tk.Checkbutton(options_frame, text="Digits (0-9)", variable=var_digits, bg="#ccadc4", font=("Helvetica", 15)).pack(anchor="w")
tk.Checkbutton(options_frame, text="Symbols (!@#...)", variable=var_symbols, bg="#ccadc4", font=("Helvetica", 15)).pack(anchor="w")

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=gen_pass, font=("Helvetica", 15, "bold"), bg="#27f67a", fg="white", padx=10, pady=5)
generate_button.pack(pady=20)

# Password Display
pass_display = tk.Entry(root, font=("Consolas", 15), justify="center", bd=2, relief="sunken", width=30, state='readonly', bg="#aaf627", fg="#f60303")
pass_display.pack(pady=10)

# Run the app
root.mainloop()
