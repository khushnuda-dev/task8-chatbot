# chatbot.py
"""
A Simple Rule-Based Chatbot
Author: [Your Name]
Description: This chatbot uses if-else conditions to respond to user queries.
"""

def chatbot():
    print("🤖 Hello! I'm ChatPy, your friendly chatbot.")
    print("💡 Type 'bye' anytime to end the chat.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Bot: Hi there! How can I help you today?")
        elif "how are you" in user_input:
            print("Bot: I'm doing great! Thanks for asking. How about you?")
        elif user_input in ["i am fine", "i am good", "fine", "good"]:
            print("Bot: That’s wonderful to hear!")
        elif "your name" in user_input:
            print("Bot: I'm ChatPy, a simple Python chatbot created with if-else logic.")
        elif "help" in user_input:
            print("Bot: I can chat with you and answer simple questions. Try asking me about my name or how I'm doing!")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day! 👋")
            break
        else:
            print("Bot: Hmm, I’m not sure how to respond to that. Can you try asking something else?")

if __name__ == "__main__":
    chatbot()