import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    length = length_var.get()
    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "No character sets selected!")
        return

    password = ''.join(secrets.choice(chars) for _ in range(length))
    result_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("🔑 Beautiful Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Variables
length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

# Widgets
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
tk.Scale(root, from_=6, to=32, orient="horizontal", variable=length_var).pack()

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor="w", padx=20)

tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

tk.Entry(root, textvariable=result_var, font=("Courier", 12), width=30, justify="center").pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white").pack(pady=5)

root.mainloop()
