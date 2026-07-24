import pandas as pd
from data_loader import fetch_stock_data
from preprocess import preprocess_data, create_sequences
from model import build_lstm

def train_model(ticker="AAPL", start="2020-01-01", end="2023-01-01"):
    df = fetch_stock_data(ticker, start, end)
    scaled, scaler = preprocess_data(df)
    X, y = create_sequences(scaled)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    model = build_lstm((X.shape[1], 1))
    model.fit(X, y, epochs=10, batch_size=32)
    return model, scaler

if __name__ == "__main__":
    model, scaler = train_model()
    model.save("data/processed/lstm_model.h5")
