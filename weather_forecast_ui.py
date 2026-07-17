import requests
import customtkinter as ctk

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

def get_weather():
    city = city_var.get().strip()
    if not city:
        result_label.configure(text="⚠ Please enter a city!", text_color="red")
        return
    
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        forecast_text = f"📍 City: {city.capitalize()}\n\n"
        
        # Show forecast every 8 steps (~24 hours)
        for i in range(0, len(data["list"]), 8):
            day = data["list"][i]
            date = day["dt_txt"].split(" ")[0]
            temp = day["main"]["temp"]
            desc = day["weather"][0]["description"].capitalize()
            humidity = day["main"]["humidity"]
            wind = day["wind"]["speed"]
            
            forecast_text += f"📅 {date}\n🌡 Temp: {temp}°C\n☁ {desc}\n💧 Humidity: {humidity}%\n🌬 Wind: {wind} m/s\n\n"
        
        result_label.configure(text=forecast_text, text_color="white")
    except Exception as e:
        result_label.configure(text=f"❌ Error: {e}", text_color="red")

# Modern UI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🌤 5-Day Weather Forecast")
app.geometry("500x500")

city_var = ctk.StringVar()

ctk.CTkLabel(app, text="Enter City Name").pack(pady=10)
ctk.CTkEntry(app, textvariable=city_var, width=250).pack(pady=5)

ctk.CTkButton(app, text="Get Forecast", command=get_weather).pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

app.mainloop()
