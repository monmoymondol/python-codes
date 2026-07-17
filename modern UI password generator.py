import secrets
import string
import customtkinter as ctk

def generate_password():
    length = int(length_var.get())
    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    chars = string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation

    if not chars:
        result_var.set("⚠ No character sets selected!")
        return

    password = ''.join(secrets.choice(chars) for _ in range(length))
    result_var.set(password)

# Modern UI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🔑 Modern Password Generator")
app.geometry("400x350")

length_var = ctk.StringVar(value="12")
upper_var = ctk.BooleanVar(value=True)
digits_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=True)
result_var = ctk.StringVar()

ctk.CTkLabel(app, text="Password Length").pack(pady=5)
ctk.CTkEntry(app, textvariable=length_var).pack(pady=5)

ctk.CTkCheckBox(app, text="Include Uppercase", variable=upper_var).pack()
ctk.CTkCheckBox(app, text="Include Digits", variable=digits_var).pack()
ctk.CTkCheckBox(app, text="Include Symbols", variable=symbols_var).pack()

ctk.CTkButton(app, text="Generate Password", command=generate_password).pack(pady=10)
ctk.CTkEntry(app, textvariable=result_var, width=300).pack(pady=10)

app.mainloop()
