import time
import threading
import customtkinter as ctk
from playsound import playsound

def start_timer():
    try:
        total_seconds = int(min_var.get()) * 60 + int(sec_var.get())
        if total_seconds <= 0:
            result_label.configure(text="⚠ Enter a valid time!", text_color="red")
            return
        
        result_label.configure(text="⏳ Timer started...", text_color="white")
        threading.Thread(target=run_timer, args=(total_seconds,), daemon=True).start()
    except ValueError:
        result_label.configure(text="⚠ Invalid input!", text_color="red")

def run_timer(total_seconds):
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_label.configure(text=f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        total_seconds -= 1
    
    timer_label.configure(text="00:00")
    result_label.configure(text="🔔 Time's up!", text_color="red")
    threading.Thread(target=lambda: playsound("alarm.mp3"), daemon=True).start()

# Modern UI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("⏳ Countdown Timer")
app.geometry("400x300")

min_var = ctk.StringVar(value="0")
sec_var = ctk.StringVar(value="30")

ctk.CTkLabel(app, text="Minutes").pack(pady=5)
ctk.CTkEntry(app, textvariable=min_var).pack(pady=5)

ctk.CTkLabel(app, text="Seconds").pack(pady=5)
ctk.CTkEntry(app, textvariable=sec_var).pack(pady=5)

ctk.CTkButton(app, text="Start Timer", command=start_timer).pack(pady=10)

timer_label = ctk.CTkLabel(app, text="00:00", font=("Arial", 48))
timer_label.pack(pady=20)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

app.mainloop()
