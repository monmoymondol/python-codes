import customtkinter as ctk

contacts = []

def add_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    email = email_var.get().strip()
    
    if not name or not phone:
        result_label.configure(text="⚠ Name and Phone are required!", text_color="red")
        return
    
    contacts.append({"name": name, "phone": phone, "email": email})
    update_list()
    result_label.configure(text="✅ Contact added!", text_color="green")

def update_list():
    listbox.delete("0.0", "end")
    for c in contacts:
        listbox.insert("end", f"{c['name']} - {c['phone']} ({c['email']})\n")

def search_contact():
    query = search_var.get().strip().lower()
    listbox.delete("0.0", "end")
    for c in contacts:
        if query in c['name'].lower() or query in c['phone'] or query in c['email'].lower():
            listbox.insert("end", f"{c['name']} - {c['phone']} ({c['email']})\n")

# Modern UI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("📒 Contact Book")
app.geometry("500x500")

# Variables
name_var = ctk.StringVar()
phone_var = ctk.StringVar()
email_var = ctk.StringVar()
search_var = ctk.StringVar()

# Input fields
ctk.CTkLabel(app, text="Name").pack(pady=5)
ctk.CTkEntry(app, textvariable=name_var).pack(pady=5)

ctk.CTkLabel(app, text="Phone").pack(pady=5)
ctk.CTkEntry(app, textvariable=phone_var).pack(pady=5)

ctk.CTkLabel(app, text="Email").pack(pady=5)
ctk.CTkEntry(app, textvariable=email_var).pack(pady=5)

ctk.CTkButton(app, text="Add Contact", command=add_contact).pack(pady=10)

result_label = ctk.CTkLabel(app, text="")
result_label.pack()

# Search
ctk.CTkLabel(app, text="Search").pack(pady=5)
ctk.CTkEntry(app, textvariable=search_var).pack(pady=5)
ctk.CTkButton(app, text="Search", command=search_contact).pack(pady=5)

# Contact list
listbox = ctk.CTkTextbox(app, width=400, height=200)
listbox.pack(pady=10)

app.mainloop()
