import matplotlib.pyplot as plt

def plot_predictions(actual, predicted, title="Stock Price Prediction"):
    plt.figure(figsize=(10,6))
    plt.plot(actual, label="Actual")
    plt.plot(predicted, label="Predicted")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
