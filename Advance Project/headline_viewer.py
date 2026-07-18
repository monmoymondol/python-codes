import requests
import customtkinter as ctk

API_KEY = "YOUR_NEWSAPI_KEY"  # get from https://newsapi.org
BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(category="general", country="us"):
    params = {
        "apiKey": API_KEY,
        "category": category,
        "country": country,
        "pageSize": 5
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if data.get("status") != "ok":
        return ["⚠ Error fetching news"]
    return [f"• {a['title']}\n{a['url']}" for a in data["articles"]]

def show_news():
    category = category_var.get()
    headlines = fetch_news(category)
    news_box.delete("0.0", "end")
    for h in headlines:
        news_box.insert("end", h + "\n\n")

# ---------------- UI Setup ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("📰 News Arranger")
app.geometry("700x500")

category_var = ctk.StringVar(value="technology")

ctk.CTkLabel(app, text="Select News Category").pack(pady=10)
ctk.CTkOptionMenu(app, variable=category_var,
                  values=["general", "technology", "sports", "business", "health", "science", "entertainment"]).pack(pady=10)

ctk.CTkButton(app, text="Fetch News", command=show_news).pack(pady=10)

news_box = ctk.CTkTextbox(app, width=600, height=300)
news_box.pack(pady=20)

app.mainloop()
