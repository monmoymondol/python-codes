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
    result_label.configure(text="✅ Invoice created with auto-number!", text_color="green")
