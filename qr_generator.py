import qrcode

def generate_qr(data, filename="qrcode.png"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls size (1 = small, 40 = large)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
        box_size=10,  # size of each box
        border=4,  # border thickness
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")

# CLI demo
if __name__ == "__main__":
    text = input("Enter text or URL: ")
    generate_qr(text, "my_qrcode.png")
