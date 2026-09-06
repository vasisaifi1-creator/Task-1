"""
Project 1: Rule-Based AI Chatbot
DecodeLabs - Industrial Training Kit

WHAT THIS PROGRAM DOES
-----------------------
This is a simple chatbot that does NOT use any machine learning or
"deep learning". It works on pure CONTROL FLOW and LOGIC:

    1. It keeps asking the user for input in an infinite loop (while True).
    2. It cleans (sanitizes) whatever the user types.
    3. It looks up the cleaned text in a dictionary (our "knowledge base")
       to decide what to reply.
    4. If nothing matches, it gives a default fallback reply.
    5. If the user types an exit word, the loop breaks and the program ends.

This mirrors the "IPO Model" from the slides:
    INPUT (get & clean text) -> PROCESS (match it to a rule) -> OUTPUT (reply)
"""

import random

# GitHub Repository: https://github.com/vasisaifi1-creator/Task-1

# ---------------------------------------------------------------------------
# STEP 1: THE KNOWLEDGE BASE
# ---------------------------------------------------------------------------
# Instead of a long, slow if/elif/elif/elif ladder (the "anti-pattern" shown
# in the slides), we use a DICTIONARY. Dictionary lookups are near-instant
# (O(1)) no matter how many rules we add, whereas an if-elif chain gets
# slower the more rules you add (O(n)).
#
# Each KEY is a list of words/phrases the user might type (an "intent").
# Each VALUE is a list of possible bot replies (we pick one at random so
# the bot feels a little less robotic).

knowledge_base = {
    "greeting": {
        "triggers": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hi there!", "Hello! How can I help you today?", "Hey! Good to see you."]
    },
    "how_are_you": {
        "triggers": ["how are you", "how are you doing", "how's it going"],
        "responses": ["I'm just a program, but I'm running smoothly! And you?"]
    },
    "name": {
        "triggers": ["what is your name", "who are you", "your name"],
        "responses": ["I'm DecodeBot, a rule-based chatbot built for Project 1!"]
    },
    "thanks": {
        "triggers": ["thanks", "thank you", "thx"],
        "responses": ["You're welcome!", "Anytime!", "Happy to help."]
    },
    "help": {
        "triggers": ["help", "what can you do", "options"],
        "responses": ["I can chat about greetings, my name,how I am doing and I'll say goodbye when you're done. Try 'bye'!"]
    },
    "current_weather": {
    "triggers": [
        "current weather",
        "weather now",
        "how's the weather now",
        "what's the weather right now",
        "current temperature",
        "temperature now",
        "today's weather"
    ],
    "responses": [
        "I'm currently a simple intent-based chatbot, so I can't provide live weather updates yet. I'm continuously learning new capabilities, and I hope to support this feature soon. Thank you for your patience!",
        "I appreciate your question! At the moment, I'm an intent-based chatbot and don't have access to real-time weather information. I'm actively being improved, so please check back soon.",
        "I'm still learning and expanding my abilities. Right now, I can't fetch live weather data, but I'm working toward supporting features like this in the future. Thanks for your understanding!"]
    },
    "time": {
    "triggers": [
        "what time is it",
        "current time",
        "time now",
        "tell me the time",
        "local time"
    ],
    "responses": [
        "I don't have access to the current time yet, but I'm learning to support features like this.",
        "Real-time information isn't available to me at the moment. Thanks for your patience!"]
    },
    "date": {
    "triggers": [
        "what is today's date",
        "today's date",
        "current date",
        "date today",
        "what day is it"
    ],
    "responses": [
        "I can't check the current date yet, but I'm working on adding real-time features.",
        "Sorry, I don't have access to the current date at the moment."]
    },
    "creator": {
    "triggers": [
        "who made you",
        "who created you",
        "who developed you",
        "who is your developer",
        "who built you"
    ],
    "responses": [
        "I was created by my developer as a learning project.",
        "I'm a chatbot built for learning and experimentation.",
        "My developer is continuously improving my capabilities."]
    },
    "bye": {
        # This is our "kill command" intent, handled specially in the loop below.
        "triggers": ["bye", "exit", "quit", "goodbye", "see you"],
        "responses": ["Goodbye! Have a great day.", "See you next time!"]
    },
    
}


# ---------------------------------------------------------------------------
# STEP 2: SANITIZATION (INPUT / PHASE 1 from the slides)
# ---------------------------------------------------------------------------
def clean_input(raw_text: str) -> str:    # : str is a type hint and -> is also a type hint
    """
    Raw human input is messy: 'Hello', 'hello', ' HELLO  ' should all be
    treated the same. We normalize by:
      - lowercasing everything            -> .lower()
      - trimming leading/trailing spaces   -> .strip()
    """
    return raw_text.lower().strip()


# ---------------------------------------------------------------------------
# STEP 3: INTENT MATCHING (PROCESS / Logic Skeleton)
# ---------------------------------------------------------------------------
def find_intent(clean_text: str):
    """
    Loops through each intent in the knowledge base and checks whether
    any of its trigger phrases appear inside what the user typed.

    Returns the intent name (e.g. "greeting") if found, otherwise None.
    Using 'in' lets us match phrases even inside a longer sentence,
    e.g. "hey there, how are you" still matches "how are you".
    """
    for intent_name, intent_data in knowledge_base.items():
        for trigger in intent_data["triggers"]:
            if trigger in clean_text:
                return intent_name
    return None


# ---------------------------------------------------------------------------
# STEP 4: RESPONSE GENERATION (OUTPUT)
# ---------------------------------------------------------------------------
def get_response(intent_name: str) -> str:
    """
    Given a matched intent, randomly picks one of its pre-written replies.
    This is the ".get()-style" idea from the slides: a single, clean lookup
    instead of a fallback wrapped in more if/else statements.
    """
    return random.choice(knowledge_base[intent_name]["responses"])


# ---------------------------------------------------------------------------
# STEP 5: THE MAIN LOOP (THE HEARTBEAT)
# ---------------------------------------------------------------------------
def run_chatbot():
    print("DecodeBot: Hello! Type 'bye' or 'exit' whenever you want to stop.\n")

    while True:                              # infinite loop = the chatbot "stays alive"
        raw_input_text = input("You : ")      # 1. get raw input
        text = clean_input(raw_input_text)   # 2. sanitize it

        if text == "":                       # handle empty input gracefully
            print("DecodeBot: Please type something.")
            continue

        intent = find_intent(text)           # 3. try to match a rule

        if intent == "bye":                  # 4. the "kill command"
            print(f"DecodeBot: {get_response('bye')}")
            break                             # exits the while loop -> program ends

        elif intent is not None:             # 5. a rule matched
            print(f"DecodeBot: {get_response(intent)}")

        else:                                 # 6. fallback for unknown input
            print("DecodeBot: I do not understand that yet. Try 'help' to see what I can do.")


# ---------------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    run_chatbot()