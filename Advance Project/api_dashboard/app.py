from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.secret_key = "secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dashboard.db"
db = SQLAlchemy(app)

from models import User

# Example APIs
WEATHER_API = "https://api.open-meteo.com/v1/forecast?latitude=23.7&longitude=90.4&current_weather=true"
CRYPTO_API = "https://api.coindesk.com/v1/bpi/currentprice.json"

@app.route("/")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    # Weather
    weather_data = requests.get(WEATHER_API).json()
    temperature = weather_data["current_weather"]["temperature"]

    # Crypto
    crypto_data = requests.get(CRYPTO_API).json()
    btc_price = crypto_data["bpi"]["USD"]["rate"]

    return render_template("dashboard.html",
                           temperature=temperature,
                           btc_price=btc_price)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session["user"] = username
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
