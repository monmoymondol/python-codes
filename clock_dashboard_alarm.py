import time
import math
import pytz
import datetime
import tkinter as tk
import customtkinter as ctk
from playsound import playsound
import threading

# List of world cities with timezones
WORLD_CITIES = {
    "Dhaka": "Asia/Dhaka",
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney"
}

alarms = []

def update_time():
    # Local digital clock
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")
    digital_label.configure(text=current_time)
    date_label.configure(text=current_date)

    # Analog clock
    canvas.delete("hands")
    now = time.localtime()
    sec = now.tm_sec
    minute = now.tm_min
    hour = now.tm_hour % 12

    sec_angle = math.radians(sec * 6 - 90)
    min_angle = math.radians(minute * 6 - 90)
    hour_angle = math.radians(hour * 30 + minute * 0.5 - 90)

    canvas.create_line(150, 150, 150 + 90*math.cos(sec_angle), 150 + 90*math.sin(sec_angle), fill="red", tags="hands")
    canvas.create_line(150, 150, 150 + 70*math.cos(min_angle), 150 + 70*math.sin(min_angle), width=3, fill="blue", tags="hands")
    canvas.create_line(150, 150, 150 + 50*math.cos(hour_angle), 150 + 50*math.sin(hour_angle), width=5, fill="white", tags="hands")

    # World clock
    city = city_var.get()
    if city in WORLD_CITIES:
        tz = pytz.timezone(WORLD_CITIES[city])
        city_time = datetime.datetime.now(tz).strftime("%H:%M:%S")
        world_label.configure(text=f"{city}: {city_time}")

    # Alarm check
    check_alarms()

    digital_label.after(1000, update_time)

def check_alarms():
    now = datetime.datetime.now().strftime("%H:%M")
    for alarm in alarms:
        if alarm == now:
            alarm_label.configure(text=f"🔔 Alarm! {alarm}", text_color="red")
            # Play sound in a separate thread so UI doesn't freeze
            threading.Thread(target=lambda: playsound("alarm.mp3"), daemon=True).start()

def set_alarm():
    alarm_time = alarm_var.get().strip()
    if alarm_time:
        alarms.append(alarm_time)
        alarm_label.configure(text=f"✅ Alarm set for {alarm_time}", text_color="green")

# Modern UI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("⚡ Advanced Clock Dashboard with Sound Alarm")
app.geometry("700x600")

# Digital clock
digital_label = ctk.CTkLabel(app, text="", font=("Arial", 48))
digital_label.pack(pady=10)

date_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
date_label.pack(pady=5)

# Analog clock canvas
canvas = tk.Canvas(app, width=300, height=300, bg="black", highlightthickness=0)
canvas.pack(pady=20)

for i in range(12):
    angle = math.radians(i*30 - 90)
    x = 150 + 120*math.cos(angle)
    y = 150 + 120*math.sin(angle)
    canvas.create_text(x, y, text=str(i if i!=0 else 12), fill="white", font=("Arial", 12))

# World clock selector
city_var = ctk.StringVar(value="Dhaka")
ctk.CTkLabel(app, text="🌍 Select City").pack(pady=5)
ctk.CTkOptionMenu(app, variable=city_var, values=list(WORLD_CITIES.keys())).pack(pady=5)
world_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
world_label.pack(pady=10)

# Alarm system
alarm_var = ctk.StringVar()
ctk.CTkLabel(app, text="⏰ Set Alarm (HH:MM)").pack(pady=5)
ctk.CTkEntry(app, textvariable=alarm_var).pack(pady=5)
ctk.CTkButton(app, text="Set Alarm", command=set_alarm).pack(pady=5)
alarm_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
alarm_label.pack(pady=10)

update_time()
app.mainloop()
