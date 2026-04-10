from agent_graph import app

def chat():
    print("Agent: Hi! How can I help you today?")

    while True:
        user_input = input("You: ")

        # Send input into LangGraph agent
        result = app.invoke({
            "user_input": user_input,
            "intent": "",
            "response": "",
            "name": "",
            "email": "",
            "platform": ""
        })

        # Print response from graph
        print(f"Agent: {result['response']}")

        # Exit after lead capture
        if result["intent"] == "high_intent":
            break


if __name__ == "__main__":
    chat()