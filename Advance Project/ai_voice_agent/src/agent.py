from wake_word import listen_for_wake_word
from speech_to_text import listen
from nlp_engine import process
from text_to_speech import speak
from integrations.weather_api import get_weather
from integrations.stock_api import get_stock_price
from integrations.calendar_api import get_next_event

def run_agent():
    while True:
        listen_for_wake_word("hey agent")
        text = listen().lower()

        if "weather" in text:
            response = get_weather("Dhaka")
        elif "stock" in text:
            response = get_stock_price("AAPL")
        elif "calendar" in text:
            response = get_next_event()
        elif text in ["quit", "exit", "stop"]:
            response = "Goodbye!"
            speak(response)
            break
        else:
            response = process(text)

        print(f"🤖 Agent: {response}")
        speak(response)

if __name__ == "__main__":
    run_agent()
