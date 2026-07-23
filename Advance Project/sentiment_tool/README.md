# 🧠 Sentiment Analysis Tool

A simple Python tool for analyzing sentiment in text.  
Supports both **command-line usage** and a **FastAPI web API**.

---

## 🚀 Features
- Detects **Positive**, **Negative**, or **Neutral** sentiment.
- Returns **polarity** (-1 to +1) and **subjectivity** (0 to 1).
- CLI for quick analysis.
- REST API for integration with other apps.

---

## 📂 Project Structure


sentiment_tool/
├── src/
│   ├── sentiment_analyzer.py   # core logic
│   ├── app.py                  # FastAPI web API
│   └── cli.py                  # command-line interface
├── requirements.txt
├── README.md
└── tests/
    └── test_sentiment.py

---

## ⚙️ Installation
```bash
pip install -r requirements.txt
```
## 🎮 Usage

CLI

python src/cli.py "I love this product!"

Output:

Text: I love this product!
Sentiment: Positive (polarity=0.50, subjectivity=0.60)

API

uvicorn src.app:app --reload --port 8000

Test:

curl -X POST http://localhost:8000/analyze -H "Content-Type: application/json" -d '{"text":"This is terrible."}'

Response
{
  "text": "This is terrible.",
  "polarity": -1.0,
  "subjectivity": 1.0,
  "label": "Negative"
}

---

👉 This gives you a **ready-to-run sentiment analysis tool** with both CLI and API. Would you like me to also add a **simple React frontend** so you can paste text into a web page and see the sentiment instantly?
