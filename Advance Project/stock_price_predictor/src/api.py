from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict_stock

app = FastAPI(title="Stock Price Predictor")

class PredictRequest(BaseModel):
    ticker: str
    days: int

@app.post("/predict")
def predict(req: PredictRequest):
    result = predict_stock(req.ticker, req.days)
    return {"ticker": req.ticker, "predictions": result}
