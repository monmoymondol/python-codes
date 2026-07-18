from jinja2 import Environment, FileSystemLoader
import pdfkit

def generate_invoice(data, output_file="invoice.pdf"):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("invoice_template.html")
    html_content = template.render(data)

    # Convert HTML to PDF
    pdfkit.from_string(html_content, output_file)
    print(f"✅ Invoice generated: {output_file}")
