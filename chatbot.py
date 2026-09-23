def chatbot():
    print("chatbot: I'm your chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("you:  ").lower().strip()

        if(user_input == "hi"  or user_input == "hello"):
            print("chatbot: HI!")
        elif(user_input == "how are you"):
            print("chatbot: I'm fine. What about you?")
        elif(user_input == "I'm fine" or user_input == "i'm also fine"):
            print("chatbot: Good.")
        elif(user_input == "who are you?"):
            print("chatbot: I'm your personal chatbot")
        elif(user_input == "bye"):
            print("chatbot: Goodbye!")
            break
        else:
            print("chatbot: sorry. I didn't understand that")

chatbot()

    