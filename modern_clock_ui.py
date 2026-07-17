import time
import tkinter as tk
import customtkinter as ctk
import math

def update_time():
    # Digital clock
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
    
    # Calculate angles
    sec_angle = math.radians(sec * 6 - 90)
    min_angle = math.radians(minute * 6 - 90)
    hour_angle = math.radians(hour * 30 + minute * 0.5 - 90)
    
    # Draw hands
    canvas.create_line(150, 150, 150 + 90*math.cos(sec_angle), 150 + 90*math.sin(sec_angle), fill="red", tags="hands")
    canvas.create_line(150, 150, 150 + 70*math.cos(min_angle), 150 + 70*math.sin(min_angle), width=3, fill="blue", tags="hands")
    canvas.create_line(150, 150, 150 + 50*math.cos(hour_angle), 150 + 50*math.sin(hour_angle), width=5, fill="white", tags="hands")
    
    digital_label.after(1000, update_time)

# Modern UI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("⏰ Modern Clock")
app.geometry("600x400")

# Digital clock
digital_label = ctk.CTkLabel(app, text="", font=("Arial", 48))
digital_label.pack(pady=10)

date_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
date_label.pack(pady=5)

# Analog clock canvas
canvas = tk.Canvas(app, width=300, height=300, bg="black", highlightthickness=0)
canvas.pack(pady=20)

# Draw clock face
for i in range(12):
    angle = math.radians(i*30 - 90)
    x = 150 + 120*math.cos(angle)
    y = 150 + 120*math.sin(angle)
    canvas.create_text(x, y, text=str(i if i!=0 else 12), fill="white", font=("Arial", 12))

update_time()
app.mainloop()
