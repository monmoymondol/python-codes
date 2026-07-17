from flask import Flask, request, redirect, render_template_string
import sqlite3
import string
import random

app = Flask(__name__)

# Database setup
conn = sqlite3.connect("urls.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT NOT NULL,
    short_code TEXT UNIQUE NOT NULL
)
""")
conn.commit()

# Generate random short code
def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Shorten URL
def shorten_url(original_url):
    code = generate_code()
    cursor.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)", (original_url, code))
    conn.commit()
    return code

# Expand URL
def expand_url(code):
    cursor.execute("SELECT original_url FROM urls WHERE short_code=?", (code,))
    result = cursor.fetchone()
    return result[0] if result else None

# ---------------- Flask Routes ----------------
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        original_url = request.form["url"]
        code = shorten_url(original_url)
        short_url = request.host_url + code
        return render_template_string(TEMPLATE, short_url=short_url)
    return render_template_string(TEMPLATE)

@app.route("/<code>")
def redirect_url(code):
    original = expand_url(code)
    if original:
        return redirect(original)
    return "⚠ Short code not found!", 404

# ---------------- HTML Template ----------------
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>URL Shortener</title>
    <style>
        body { font-family: Arial; background: #222; color: #eee; text-align: center; padding: 50px; }
        input { padding: 10px; width: 300px; }
        button { padding: 10px 20px; margin-top: 10px; }
        .result { margin-top: 20px; font-size: 18px; color: #0f0; }
    </style>
</head>
<body>
    <h1>🔗 URL Shortener</h1>
    <form method="POST">
        <input type="text" name="url" placeholder="Enter URL" required>
        <br>
        <button type="submit">Shorten</button>
    </form>
    {% if short_url %}
        <div class="result">✅ Shortened URL: <a href="{{ short_url }}" target="_blank">{{ short_url }}</a></div>
    {% endif %}
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
