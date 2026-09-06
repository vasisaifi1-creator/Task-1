# 🤖 DecodeBot — Rule-Based AI Chatbot

A simple, lightweight chatbot built in Python using **pure control flow and logic** — no machine learning, no external APIs, no dataset. It matches user input against a dictionary-based knowledge base and replies accordingly.

> Built as part of the DecodeLabs Industrial Training Kit — Project 1

## 🔗 Repository

https://github.com/vasisaifi1-creator/Task-1

## 🧠 How It Works

The chatbot follows the classic **IPO Model**:

1. Continuously asks the user for input inside a `while True` loop
2. **Sanitizes** the input — lowercases and trims extra spaces
3. **Matches** the cleaned text against trigger phrases in a dictionary (knowledge base)
4. **Responds** with a randomly chosen reply for that intent (feels less repetitive)
5. If no match is found, it gives a fallback message
6. Typing an exit word (`bye`, `exit`, `quit`, etc.) ends the conversation

Using a **dictionary** instead of a long `if/elif` chain makes lookups near-instant (O(1)) no matter how many intents are added — unlike an if-elif ladder, which slows down as more rules are added (O(n)).

## ✨ Features / Supported Intents

| Intent | Example triggers | What it does |
|---|---|---|
| Greeting | `hi`, `hello`, `hey`, `good morning` | Greets the user |
| How are you | `how are you`, `how's it going` | Responds about its status |
| Name | `what is your name`, `who are you` | Introduces itself |
| Thanks | `thanks`, `thank you`, `thx` | Acknowledges gratitude |
| Help | `help`, `what can you do`, `options` | Lists what it can do |
| Current weather | `current weather`, `weather now` | Explains it can't fetch live weather (yet) |
| Time | `what time is it`, `current time` | Explains it can't fetch live time (yet) |
| Date | `today's date`, `what day is it` | Explains it can't fetch live date (yet) |
| Creator | `who made you`, `who created you` | Talks about its developer |
| Bye | `bye`, `exit`, `quit`, `goodbye` | Ends the conversation |

Matching works even inside longer sentences — e.g. *"hey there, how are you"* still correctly matches the `how_are_you` intent, since it checks whether the trigger phrase appears **anywhere** in the input.

## 🛠️ Built With

- Python 3 (standard library only — just `random`)
- Core concepts: control flow, functions, loops, dictionaries, string processing, type hints

## 🚀 How to Run

1. Clone this repository
```bash
   git clone https://github.com/vasisaifi1-creator/Task-1
```
2. Navigate into the folder
```bash
   cd Task-1
```
3. Run the chatbot
```bash
   python Chatbot.py
```

## 💬 Example Conversation

DecodeBot: Hello! Type 'bye' or 'exit' whenever you want to stop.
You : hi
DecodeBot: Hello! How can I help you today?

You : what is your name
DecodeBot: I'm DecodeBot, a rule-based chatbot built for Project 1!

You : who made you
DecodeBot: I was created by my developer as a learning project.

You : what time is it
DecodeBot: I don't have access to the current time yet, but I'm learning to support features like this.

You : thanks
DecodeBot: You're welcome!

You : bye
DecodeBot: Goodbye! Have a great day.


## 🔍 Code Overview

| Function | Purpose |
|---|---|
| `clean_input()` | Normalizes user input (lowercase + strip whitespace) |
| `find_intent()` | Loops through the knowledge base to find a matching intent |
| `get_response()` | Randomly picks a reply for the matched intent |
| `run_chatbot()` | Main loop that ties everything together |

## 🔮 Future Improvements

- Add live weather, time, and date support via APIs
- Add more intents and conversational variety
- Add a simple GUI using Tkinter
- Replace exact-phrase matching with lightweight NLP-based matching

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 👤 Author

**MOHD VASI SAIFI**
GitHub: [@vasisaifi1-creator](https://github.com/vasisaifi1-creator)
