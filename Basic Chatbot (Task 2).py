import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How about you?", "I'm just a chatbot, but I'm functioning properly!"]
    ],
    [
        r"(.*) your name ?",
        ["I'm a chatbot created to assist you!", "You can call me ChatBot!"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, answer simple questions, and keep you entertained!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "See you next time!"]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()