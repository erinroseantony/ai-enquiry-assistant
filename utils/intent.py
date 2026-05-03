def detect_intent(message):
    message = message.lower()

    course_keywords = [
        "course", "learn", "study",
        "data", "ai", "web", "development"
    ]

    fee_keywords = ["fee", "fees", "price", "cost", "amount", "how much"]

    if any(word in message for word in course_keywords):
        return "course_query"

    elif any(word in message for word in fee_keywords):
        return "fee_query"

    elif any(word in message for word in ["name", "phone", "contact"]):
        return "lead_capture"

    else:
        return "unknown"