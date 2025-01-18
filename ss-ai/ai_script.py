import random
import time
from textblob import TextBlob

# ASCII Art for Oracle
ascii_art = """
 _____ __              __                   _____          
/ ___// /_  ____ _____/ /___ _      __     / ___/___  _____
\__ \/ __ \/ __ `/ __  / __ \ | /| / /_____\__ \/ _ \/ ___/
___/ / / / / /_/ / /_/ / /_/ / |/ |/ /_____/__/ /  __/ /__  
/____/_/ /_/\__,_/\__,_/\____/|__/|__/     /____/\___/\___/  
                   ___    ____                               
                  /   |  /  _/                               
                 / /| |  / /                                 
                / ___ |_/ /                                  
               /_/  |_/___/                                  
"""

# A simple memory system to store context
class Memory:
    def __init__(self):
        self.memory = {}

    def remember(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        return self.memory.get(key, "I don't remember that.")

# Initialize memory
memory = Memory()

# Enhanced conversational responses
def respond_to_input(user_input):
    # Basic sentiment analysis
    sentiment = TextBlob(user_input).sentiment.polarity
    
    # Responses based on sentiment
    if sentiment > 0.2:
        return random.choice([
            "That sounds positive! Tell me more.",
            "I'm glad to hear that!",
            "Wow, sounds great!",
        ])
    elif sentiment < -0.2:
        return random.choice([
            "I'm sorry to hear that. Do you want to talk about it?",
            "That sounds tough. I'm here for you.",
            "It seems like you're going through something difficult."
        ])
    else:
        return random.choice([
            "Got it. What else would you like to discuss?",
            "Okay, I'm listening.",
            "Interesting, tell me more!"
        ])

# Memory interaction
def interact_with_memory(user_input):
    if "remember" in user_input.lower():
        key = input("What should I remember? ")
        value = input("What should I remember about it? ")
        memory.remember(key, value)
        return f"Got it. I'll remember that {key} is {value}."
    
    elif "do you remember" in user_input.lower():
        key = input("What should I recall? ")
        return f"I remember that {key} is {memory.recall(key)}."
    
    return None

# Main conversation loop
def start_conversation():
    print(ascii_art)
    print("Welcome! You can talk to me.")
    
    while True:
        user_input = input("You: ").lower()
        
        if "exit" in user_input:
            print("Oracle: Goodbye!")
            break
        
        # Handle special memory commands
        memory_response = interact_with_memory(user_input)
        if memory_response:
            print(f"Oracle: {memory_response}")
            continue
        
        # Respond to the input
        response = respond_to_input(user_input)
        print(f"Oracle: {response}")
        time.sleep(1)

if __name__ == "__main__":
    start_conversation()
