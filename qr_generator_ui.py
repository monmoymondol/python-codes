import qrcode
from PIL import Image, ImageTk
import customtkinter as ctk

def generate_qr():
    data = input_var.get().strip()
    if not data:
        result_label.configure(text="⚠ Please enter text or URL!", text_color="red")
        return
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code
    filename = "qrcode.png"
    img.save(filename)
    
    # Display QR code in UI
    img_tk = ImageTk.PhotoImage(img)
    qr_label.configure(image=img_tk)
    qr_label.image = img_tk
    result_label.configure(text=f"✅ QR Code saved as {filename}", text_color="green")

# Modern UI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("📱 QR Code Generator")
app.geometry("500x600")

input_var = ctk.StringVar()

ctk.CTkLabel(app, text="Enter Text or URL").pack(pady=10)
ctk.CTkEntry(app, textvariable=input_var, width=400).pack(pady=10)

ctk.CTkButton(app, text="Generate QR Code", command=generate_qr).pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

qr_label = ctk.CTkLabel(app, text="")
qr_label.pack(pady=20)

app.mainloop()
