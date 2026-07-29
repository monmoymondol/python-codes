import requests

API_KEY = "YOUR_OPENWEATHER_KEY"

def get_weather(city="Dhaka"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()
    temp = res["main"]["temp"]
    desc = res["weather"][0]["description"]
    return f"The weather in {city} is {desc} with {temp}°C."
