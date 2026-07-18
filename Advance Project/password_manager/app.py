import customtkinter as ctk
from db import init_db, add_entry, get_entries
from crypto import load_key, encrypt_password, decrypt_password

init_db()
key = load_key()

def save_password():
    service = service_var.get()
    username = user_var.get()
    password = pass_var.get()
    encrypted = encrypt_password(password, key)
    add_entry(service, username, encrypted)
    result_label.configure(text="✅ Password saved!", text_color="green")
    show_passwords()

def show_passwords():
    entries = get_entries()
    listbox.delete("0.0", "end")
    for service, username, encrypted in entries:
        decrypted = decrypt_password(encrypted, key)
        listbox.insert("end", f"{service} | {username} | {decrypted}\n")

# ---------------- UI ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🔐 Password Manager")
app.geometry("600x500")

service_var = ctk.StringVar()
user_var = ctk.StringVar()
pass_var = ctk.StringVar()

ctk.CTkLabel(app, text="Service").pack(pady=5)
ctk.CTkEntry(app, textvariable=service_var).pack(pady=5)

ctk.CTkLabel(app, text="Username").pack(pady=5)
ctk.CTkEntry(app, textvariable=user_var).pack(pady=5)

ctk.CTkLabel(app, text="Password").pack(pady=5)
ctk.CTkEntry(app, textvariable=pass_var, show="*").pack(pady=5)

ctk.CTkButton(app, text="Save Password", command=save_password).pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

listbox = ctk.CTkTextbox(app, width=500, height=250)
listbox.pack(pady=10)

show_passwords()
app.mainloop()
