# Basic Chat Bot

while True:
    # First user input
    user_input = input("Say something to the chatbot: ").lower().strip()
    if user_input == "hi":
        print("Hello, Nice to meet you.")

        # Second user input
        next_input = input("Say someting to the chatbot: ").lower().strip()
        if "how are you doing" in next_input:
            print("I'm fine, thank you.")

            # Third user input
            last_input = input("Say something to the chatbot: ").lower().strip()
            if last_input == "bye":
                print("Good-bye!")
                break
            else:
                print("I was expecting you to say bye...")
        else:
            print("I was expecting you to ask how I was doing...")

    else:
        print("Please say hi to start chat.")
