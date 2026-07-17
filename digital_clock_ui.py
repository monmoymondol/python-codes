import time
import customtkinter as ctk

def update_time():
    current_time = time.strftime("%H:%M:%S")   # 24-hour format
    clock_label.configure(text=current_time)
    clock_label.after(1000, update_time)       # update every second

# Modern UI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("⏰ Digital Clock")
app.geometry("400x200")

clock_label = ctk.CTkLabel(app, text="", font=("Arial", 48))
clock_label.pack(expand=True)

update_time()  # start updating
app.mainloop()
