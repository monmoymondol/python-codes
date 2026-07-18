import customtkinter as ctk
from db import init_db, mark_attendance, get_records
from datetime import datetime

init_db()

def save_attendance():
    name = name_var.get()
    status = status_var.get()
    date = datetime.now().strftime("%Y-%m-%d")
    mark_attendance(name, date, status)
    result_label.configure(text="✅ Attendance marked!", text_color="green")
    show_records()

def show_records():
    records = get_records()
    listbox.delete("0.0", "end")
    for name, date, status in records:
        listbox.insert("end", f"{date} | {name} | {status}\n")

# ---------------- UI ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🕒 Attendance System")
app.geometry("600x500")

name_var = ctk.StringVar()
status_var = ctk.StringVar(value="Present")

ctk.CTkLabel(app, text="Name").pack(pady=5)
ctk.CTkEntry(app, textvariable=name_var).pack(pady=5)

ctk.CTkLabel(app, text="Status").pack(pady=5)
ctk.CTkOptionMenu(app, variable=status_var, values=["Present", "Absent", "Late"]).pack(pady=5)

ctk.CTkButton(app, text="Mark Attendance", command=save_attendance).pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

listbox = ctk.CTkTextbox(app, width=500, height=250)
listbox.pack(pady=10)

show_records()
app.mainloop()
