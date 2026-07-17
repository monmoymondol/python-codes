import PyPDF2
import customtkinter as ctk
from tkinter import filedialog

def merge_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if not files:
        result_label.configure(text="⚠ No files selected!", text_color="red")
        return
    
    merger = PyPDF2.PdfMerger()
    for pdf in files:
        merger.append(pdf)
    merger.write("merged.pdf")
    merger.close()
    result_label.configure(text="✅ Merged PDF saved as merged.pdf", text_color="green")

def split_pdf():
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file:
        result_label.configure(text="⚠ No file selected!", text_color="red")
        return
    
    reader = PyPDF2.PdfReader(file)
    for i in range(len(reader.pages)):
        writer = PyPDF2.PdfWriter()
        writer.add_page(reader.pages[i])
        output = f"page_{i+1}.pdf"
        with open(output, "wb") as f:
            writer.write(f)
    result_label.configure(text="✅ Split into individual pages!", text_color="green")

def extract_text():
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file:
        result_label.configure(text="⚠ No file selected!", text_color="red")
        return
    
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    result_label.configure(text="✅ Text extracted to extracted_text.txt", text_color="green")

# Modern UI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("📑 PDF Manager")
app.geometry("500x400")

ctk.CTkButton(app, text="Merge PDFs", command=merge_pdfs).pack(pady=10)
ctk.CTkButton(app, text="Split PDF", command=split_pdf).pack(pady=10)
ctk.CTkButton(app, text="Extract Text", command=extract_text).pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=20)

app.mainloop()
