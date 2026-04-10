def detect_intent(user_input):
    user_input = user_input.lower()

    # HIGH INTENT FIRST (priority)
    if any(word in user_input for word in ["buy", "subscribe", "sign up", "try", "interested"]):
        return "high_intent"

    elif any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in user_input for word in ["price", "cost", "plan", "pricing"]):
        return "pricing"

    else:
        return "unknown"