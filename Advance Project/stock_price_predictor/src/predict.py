import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from data_loader import fetch_stock_data
from preprocess import preprocess_data, create_sequences

def predict_stock(ticker="AAPL", days=7):
    df = fetch_stock_data(ticker, "2020-01-01", "2023-01-01")
    scaled, scaler = preprocess_data(df)
    model = load_model("data/processed/lstm_model.h5")

    last_seq = scaled[-60:]
    predictions = []
    current_seq = last_seq.reshape((1, 60, 1))

    for _ in range(days):
        pred = model.predict(current_seq)[0][0]
        predictions.append(pred)
        current_seq = np.append(current_seq[:,1:,:], [[[pred]]], axis=1)

    return scaler.inverse_transform(np.array(predictions).reshape(-1,1)).flatten().tolist()

if __name__ == "__main__":
    print(predict_stock("AAPL", 7))
