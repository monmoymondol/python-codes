import customtkinter as ctk

expenses = []

def add_expense():
    name = name_var.get()
    amount = float(amount_var.get())
    category = category_var.get()
    expenses.append({"name": name, "amount": amount, "category": category})
    update_list()

def update_list():
    total = sum(exp["amount"] for exp in expenses)
    listbox.delete(0, "end")
    for exp in expenses:
        listbox.insert("end", f"{exp['name']} - {exp['amount']} ({exp['category']})")
    total_label.configure(text=f"Total: {total:.2f}")

# Modern UI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("💰 Expense Tracker")
app.geometry("500x400")

name_var = ctk.StringVar()
amount_var = ctk.StringVar()
category_var = ctk.StringVar()

ctk.CTkLabel(app, text="Expense Name").pack(pady=5)
ctk.CTkEntry(app, textvariable=name_var).pack(pady=5)

ctk.CTkLabel(app, text="Amount").pack(pady=5)
ctk.CTkEntry(app, textvariable=amount_var).pack(pady=5)

ctk.CTkLabel(app, text="Category").pack(pady=5)
ctk.CTkEntry(app, textvariable=category_var).pack(pady=5)

ctk.CTkButton(app, text="Add Expense", command=add_expense).pack(pady=10)

listbox = ctk.CTkTextbox(app, width=400, height=150)
listbox.pack(pady=10)

total_label = ctk.CTkLabel(app, text="Total: 0.00", font=("Arial", 14))
total_label.pack(pady=10)

app.mainloop()
