import React from "react";
import { Line } from "react-chartjs-2";

export default function Chart({ predictions, ticker }) {
  const data = {
    labels: predictions.map((_, i) => `Day ${i + 1}`),
    datasets: [
      {
        label: `${ticker} Predicted Price`,
        data: predictions,
        borderColor: "rgba(75,192,192,1)",
        backgroundColor: "rgba(75,192,192,0.2)",
        fill: true,
        tension: 0.3
      }
    ]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: "top" },
      title: { display: true, text: "Stock Price Predictions" }
    }
  };

  return (
    <div style={{ maxWidth: "800px" }}>
      <Line data={data} options={options} />
    </div>
  );
}
