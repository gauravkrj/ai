print("Hi, I'm a chatbot. How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["hi", "hello", "hey"]:
        print("Chatbot: Hello! How can I help you today?")
    elif user_input.lower() == "what's your name?":
        print("Chatbot: My name is Chatbot.")
    elif user_input.lower() == "what do you do?":
        print("Chatbot: I help people with information and answer questions. What can I help you with today?")
    elif user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Have a great day! Bye.")
        break
    else:
        print("Chatbot: I'm sorry, I don't understand what you're saying. Can you rephrase that?")
