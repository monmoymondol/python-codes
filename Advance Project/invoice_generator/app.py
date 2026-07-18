import customtkinter as ctk
from invoice import generate_invoice

def create_invoice():
    customer = customer_var.get()
    items = items_box.get("0.0", "end").strip().split("\n")
    item_list = []
    total = 0
    for line in items:
        try:
            name, price = line.split(",")
            price = float(price)
            item_list.append({"name": name.strip(), "price": price})
            total += price
        except:
            continue

    data = {
        "customer": customer,
        "items": item_list,
        "total": total
    }
    generate_invoice(data)
    result_label.configure(text="✅ Invoice created!", text_color="green")

# ---------------- UI ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🧾 Invoice Generator")
app.geometry("600x500")

customer_var = ctk.StringVar()

ctk.CTkLabel(app, text="Customer Name").pack(pady=5)
ctk.CTkEntry(app, textvariable=customer_var).pack(pady=5)

ctk.CTkLabel(app, text="Items (format: name, price)").pack(pady=5)
items_box = ctk.CTkTextbox(app, width=500, height=200)
items_box.pack(pady=10)

ctk.CTkButton(app, text="Generate Invoice", command=create_invoice).pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

app.mainloop()
