def chatbot():
    print("Hello! How can I assist you today?")

    while True:
        user_input = input("\nYou: ").lower()

        # Exit condition
        if user_input in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Greeting responses
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")

        # Asking about the bot
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm here to help!")

        # Time query
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}")

        # Date query
        elif "date" in user_input:
            from datetime import datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {current_date}")

        # Thank you response
        elif "thank you" in user_input:
            print("Chatbot: You're welcome!")

        # Default response for unrecognized input
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase?")

# Run the chatbot
chatbot()
