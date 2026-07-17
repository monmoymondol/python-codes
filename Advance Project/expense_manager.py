import sqlite3
import customtkinter as ctk
from tkinter import filedialog
import matplotlib.pyplot as plt

# Database setup
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    date TEXT NOT NULL
)
""")
conn.commit()

# ---------------- Functions ----------------
def add_expense():
    try:
        amount = float(amount_var.get())
        category = category_var.get().strip()
        description = desc_var.get().strip()
        date = date_var.get().strip()
        
        cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                       (amount, category, description, date))
        conn.commit()
        result_label.configure(text="✅ Expense added!", text_color="green")
        update_list()
    except ValueError:
        result_label.configure(text="⚠ Amount must be a number!", text_color="red")

def update_list():
    listbox.delete("0.0", "end")
    cursor.execute("SELECT amount, category, description, date FROM expenses")
    for e in cursor.fetchall():
        listbox.insert("end", f"{e[3]} | {e[1]} | ${e[0]:.2f} | {e[2]}\n")

def show_chart():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    if not data:
        result_label.configure(text="⚠ No data for chart!", text_color="red")
        return
    
    categories = [d[0] for d in data]
    amounts = [d[1] for d in data]
    
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Expense Distribution by Category")
    plt.show()

def export_csv():
    file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files","*.csv")])
    if not file:
        return
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    with open(file, "w", encoding="utf-8") as f:
        f.write("ID,Amount,Category,Description,Date\n")
        for r in rows:
            f.write(",".join(map(str, r)) + "\n")
    result_label.configure(text=f"✅ Exported to {file}", text_color="green")

# ---------------- UI Setup ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("💰 Expense Manager")
app.geometry("700x600")

amount_var = ctk.StringVar()
category_var = ctk.StringVar()
desc_var = ctk.StringVar()
date_var = ctk.StringVar()

ctk.CTkLabel(app, text="Amount").pack(pady=5)
ctk.CTkEntry(app, textvariable=amount_var).pack(pady=5)

ctk.CTkLabel(app, text="Category").pack(pady=5)
ctk.CTkEntry(app, textvariable=category_var).pack(pady=5)

ctk.CTkLabel(app, text="Description").pack(pady=5)
ctk.CTkEntry(app, textvariable=desc_var).pack(pady=5)

ctk.CTkLabel(app, text="Date (YYYY-MM-DD)").pack(pady=5)
ctk.CTkEntry(app, textvariable=date_var).pack(pady=5)

ctk.CTkButton(app, text="Add Expense", command=add_expense).pack(pady=10)
ctk.CTkButton(app, text="Show Chart", command=show_chart).pack(pady=5)
ctk.CTkButton(app, text="Export CSV", command=export_csv).pack(pady=5)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

listbox = ctk.CTkTextbox(app, width=600, height=250)
listbox.pack(pady=10)

update_list()
app.mainloop()
