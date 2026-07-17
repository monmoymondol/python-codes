import random
import time
import threading
import customtkinter as ctk

def animate_roll(num_dice, sides):
    # Animate dice rolling for ~1.5 seconds
    for _ in range(15):
        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        total = sum(rolls)
        result_label.configure(
            text=f"🎲 Rolling... {', '.join(map(str, rolls))}\n🔢 Total: {total}",
            text_color="yellow"
        )
        time.sleep(0.1)
    
    # Final result
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    total = sum(rolls)
    result_label.configure(
        text=f"🎲 Final Rolls: {', '.join(map(str, rolls))}\n🔢 Total: {total}",
        text_color="white"
    )

def roll_dice():
    try:
        num_dice = int(dice_var.get())
        sides = int(sides_var.get())
        if num_dice <= 0 or sides <= 1:
            result_label.configure(text="⚠ Enter valid numbers!", text_color="red")
            return
        # Run animation in a separate thread
        threading.Thread(target=animate_roll, args=(num_dice, sides), daemon=True).start()
    except ValueError:
        result_label.configure(text="⚠ Invalid input!", text_color="red")

# Modern UI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🎲 Dice Roller with Animation")
app.geometry("400x300")

dice_var = ctk.StringVar(value="2")
sides_var = ctk.StringVar(value="6")

ctk.CTkLabel(app, text="Number of Dice").pack(pady=5)
ctk.CTkEntry(app, textvariable=dice_var).pack(pady=5)

ctk.CTkLabel(app, text="Sides per Die").pack(pady=5)
ctk.CTkEntry(app, textvariable=sides_var).pack(pady=5)

ctk.CTkButton(app, text="Roll Dice", command=roll_dice).pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=20)

app.mainloop()
