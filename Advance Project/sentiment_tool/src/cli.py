# cli.py
import sys
from sentiment_analyzer import analyze_sentiment

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cli.py \"Your text here\"")
        sys.exit(1)

    text = sys.argv[1]
    result = analyze_sentiment(text)
    print(f"Text: {result['text']}")
    print(f"Sentiment: {result['label']} (polarity={result['polarity']:.2f}, subjectivity={result['subjectivity']:.2f})")
