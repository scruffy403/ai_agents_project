def rule_based_chatbot(user_input):
    #  Define rules as conditions and responses
    rules = {
        "hello": "Hello! How can I help you?",
        "price": "Our prices start at $10. Let me know if you need more details!",
        "bye": "Goodbye! Have a great day!"
    }

    # Check each rule to find a matching response
    for keyword, response in rules.items():
        if keyword in user_input.lower():
            return response


    # Default response if no rules match
    return "I'm here to help with any questions you have."

# Test the chatbot
print(rule_based_chatbot("Hello there!\n"))
print(rule_based_chatbot("What is the price of your produce?\n"))
print(rule_based_chatbot("Can you tell me about shipping?\n"))
print(rule_based_chatbot("Ok thanks, bye\n"))