from jinja2 import Environment, FileSystemLoader
import pdfkit
from datetime import datetime
import os

def get_invoice_number():
    # Simple auto-increment system
    if not os.path.exists("invoice_counter.txt"):
        with open("invoice_counter.txt", "w") as f:
            f.write("1")
            return 1
    else:
        with open("invoice_counter.txt", "r+") as f:
            num = int(f.read().strip())
            new_num = num + 1
            f.seek(0)
            f.write(str(new_num))
            f.truncate()
            return new_num

def generate_invoice(data, output_file="invoice.pdf"):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("invoice_template.html")

    # Add invoice number + date
    data["invoice_number"] = get_invoice_number()
    data["date"] = datetime.now().strftime("%Y-%m-%d")

    html_content = template.render(data)
    pdfkit.from_string(html_content, output_file)
    print(f"✅ Invoice #{data['invoice_number']} generated: {output_file}")
