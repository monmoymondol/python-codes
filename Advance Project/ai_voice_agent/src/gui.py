import tkinter as tk

def run_gui():
    root = tk.Tk()
    root.title("AI Voice Agent Dashboard")

    tk.Label(root, text="AI Voice Agent Settings", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Wake Word: Hey Agent").pack()
    tk.Label(root, text="Language: English/Bangla/Hindi").pack()
    tk.Label(root, text="APIs: Weather, Stock, Calendar").pack()

    tk.Button(root, text="View Logs", command=lambda: print("Logs opened")).pack(pady=10)

    root.mainloop()
