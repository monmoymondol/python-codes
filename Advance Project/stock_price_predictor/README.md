# 📈 Stock Price Predictor

An advanced AI project for predicting stock prices using LSTM neural networks.  
Includes data pipelines, training scripts, API service, and visualization.

## 📂 Project Structure

```
stock_price_predictor/
├── data/
│   ├── raw/                  # raw stock data (CSV, API dumps)
│   ├── processed/            # cleaned datasets
│   └── features/             # engineered features
├── notebooks/                # Jupyter notebooks for exploration
├── src/
│   ├── __init__.py
│   ├── data_loader.py        # fetch data from APIs (Yahoo Finance, Alpha Vantage)
│   ├── preprocess.py         # cleaning, normalization, feature engineering
│   ├── model.py              # ML/DL models (LSTM, Prophet, XGBoost)
│   ├── train.py              # training pipeline
│   ├── predict.py            # prediction pipeline
│   ├── evaluation.py         # metrics (RMSE, MAE, MAPE)
│   ├── visualization.py      # charts (candlesticks, predictions vs actual)
│   └── api.py                # FastAPI service for predictions
├── frontend/
│   ├── web/                  # React dashboard
│   │   ├── src/
│   │   │   ├── App.js
│   │   │   ├── components/
│   │   │   │   ├── Chart.js
│   │   │   │   └── PredictionForm.js
│   │   └── package.json
├── tests/
│   ├── test_model.py
│   ├── test_preprocess.py
│   └── test_api.py
├── requirements.txt
├── README.md
└── Dockerfile

```

---

## 🚀 Features
- Fetch stock data from Yahoo Finance.
- Preprocess and normalize data.
- Train LSTM model for time series forecasting.
- Predict future stock prices.
- Serve predictions via FastAPI.
- Visualize predictions vs actual.

---

## ⚙️ Installation
```bash
pip install -r requirements.txt
```
## 🎮 Usage

Train Model

python src/train.py

Predict

python src/predict.py

API

uvicorn src.api:app --reload --port 8000

POST request:
{ "ticker": "AAPL", "days": 7 }


---

## 📄 `Dockerfile`
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```
## 🚀 How to Run
1. Start your backend:

```bash
uvicorn src.api:app --reload --port 8000
```
2. Start the frontend:
```bash
cd frontend/web
npm install
npm start
```
3. Open http://localhost:3000 in your browser.

4. Enter a ticker (e.g., AAPL) and forecast horizon (days).
The chart will display predicted prices.
```
COPY src/ ./src
COPY data/ ./data
```
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
```
