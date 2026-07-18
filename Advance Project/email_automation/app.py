import customtkinter as ctk
from emailer import send_email

def send():
    sender = sender_var.get()
    password = pass_var.get()
    recipient = recipient_var.get()
    subject = subject_var.get()
    body = body_box.get("0.0", "end")

    success = send_email(sender, password, recipient, subject, body)
    if success:
        result_label.configure(text="✅ Email sent successfully!", text_color="green")
    else:
        result_label.configure(text="⚠ Failed to send email!", text_color="red")

# ---------------- UI ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("📧 Email Automation Tool")
app.geometry("600x500")

sender_var = ctk.StringVar()
pass_var = ctk.StringVar()
recipient_var = ctk.StringVar()
subject_var = ctk.StringVar()

ctk.CTkLabel(app, text="Sender Email").pack(pady=5)
ctk.CTkEntry(app, textvariable=sender_var).pack(pady=5)

ctk.CTkLabel(app, text="Password (App Password)").pack(pady=5)
ctk.CTkEntry(app, textvariable=pass_var, show="*").pack(pady=5)

ctk.CTkLabel(app, text="Recipient Email").pack(pady=5)
ctk.CTkEntry(app, textvariable=recipient_var).pack(pady=5)

ctk.CTkLabel(app, text="Subject").pack(pady=5)
ctk.CTkEntry(app, textvariable=subject_var).pack(pady=5)

ctk.CTkLabel(app, text="Body").pack(pady=5)
body_box = ctk.CTkTextbox(app, width=500, height=200)
body_box.pack(pady=10)

ctk.CTkButton(app, text="Send Email", command=send).pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

app.mainloop()
