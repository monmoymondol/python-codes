import random
import json
from memory import MemoryManager

# Load intents
with open("intents.json") as f:
    intents = json.load(f)["intents"]

memory = MemoryManager()

def classify_intent(message):
    message = message.lower()
    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern in message:
                return intent["tag"]
    return "unknown"

def generate_response(intent):
    for intent_obj in intents:
        if intent_obj["tag"] == intent:
            return random.choice(intent_obj["responses"])
    return "Sorry, I didn’t understand that."

def chat(user_id, message):
    intent = classify_intent(message)
    response = generate_response(intent)
    memory.update_context(user_id, message, response)
    return response

# Example run
if __name__ == "__main__":
    user_id = "sagor"
    print("🤖 Chatbot ready! Type 'quit' to exit.")
    while True:
        msg = input("You: ")
        if msg.lower() == "quit":
            break
        reply = chat(user_id, msg)
        print("Bot:", reply)
