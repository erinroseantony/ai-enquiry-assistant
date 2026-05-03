import streamlit as st
from utils.intent import detect_intent
from utils.recommender import recommend_course
from utils.lead_manager import save_lead

st.set_page_config(page_title="WhatsApp AI Assistant", layout="centered")

st.markdown("""
<style>
body {
    background-color: #ece5dd;
}

.chat-container {
    max-width: 600px;
    margin: auto;
    padding: 10px;
}

.user-bubble {
    background-color: #dcf8c6;
    padding: 10px 15px;
    border-radius: 15px;
    margin: 5px;
    text-align: right;
    width: fit-content;
    margin-left: auto;
}

.bot-bubble {
    background-color: white;
    padding: 10px 15px;
    border-radius: 15px;
    margin: 5px;
    text-align: left;
    width: fit-content;
    border: 1px solid #ddd;
}

.header {
    background-color: #075e54;
    color: white;
    padding: 10px;
    font-size: 18px;
    text-align: center;
    border-radius: 10px 10px 0 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">📱 AI Enquiry Assistant (Online)</div>', unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ("bot", "👋 Hi! I'm here to help you with course details.\nYou can ask about fees, duration, or available courses!")
    ]

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f'<div class="user-bubble">{message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">{message}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

user_input = st.chat_input("Type a message...")

if user_input:
    intent = detect_intent(user_input)

    if intent in ["course_query", "fee_query"]:
        response = recommend_course(user_input)

        if not response:
            response = """
We offer:
📘 Data Science
📘 Web Development
📘 Artificial Intelligence

👉 Try:
- "data science course"
- "web dev details"
- "AI fees"
"""

    elif intent == "lead_capture":
        save_lead(user_input)
        response = "✅ Thanks! Our team will contact you soon."

    else:
        response = "❓ Can you please clarify?"


    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))

    st.rerun()