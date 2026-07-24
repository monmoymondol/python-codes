import React, { useState } from "react";

export default function PredictionForm({ onPredict }) {
  const [ticker, setTicker] = useState("AAPL");
  const [days, setDays] = useState(7);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ticker, days: parseInt(days) })
      });
      const data = await res.json();
      onPredict(data.predictions, ticker);
    } catch (err) {
      alert("Error fetching predictions: " + err.message);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <label>
        Ticker:
        <input
          type="text"
          value={ticker}
          onChange={(e) => setTicker(e.target.value)}
          style={{ marginLeft: "10px" }}
        />
      </label>
      <label style={{ marginLeft: "20px" }}>
        Days:
        <input
          type="number"
          value={days}
          onChange={(e) => setDays(e.target.value)}
          style={{ marginLeft: "10px" }}
        />
      </label>
      <button type="submit" style={{ marginLeft: "20px" }}>
        Predict
      </button>
    </form>
  );
}
