import React, { useState } from "react";
import PredictionForm from "./components/PredictionForm";
import Chart from "./components/Chart";

export default function App() {
  const [predictions, setPredictions] = useState([]);
  const [ticker, setTicker] = useState("");

  const handlePredictions = (data, ticker) => {
    setPredictions(data);
    setTicker(ticker);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>📈 Stock Price Predictor</h1>
      <PredictionForm onPredict={handlePredictions} />
      {predictions.length > 0 && (
        <Chart predictions={predictions} ticker={ticker} />
      )}
    </div>
  );
}
