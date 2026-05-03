AI Enquiry Assistant 

This project is a simple AI-powered chatbot designed to help educational institutions handle student enquiries.
It works like a WhatsApp chat where users can ask about courses, fees, and other details—and even share their contact info for follow-up.

## Why I Built This

Educational institutions often receive the same questions again and again:
* What courses are available?
* What are the fees?
* How long is the course?

Instead of answering manually every time, this assistant helps automate those conversations in a simple and user-friendly way.


## What This App Does

* 💬 Simulates a WhatsApp-style chat interface
* 📚 Shows available courses
* 💰 Provides course fees and duration
* 🧠 Understands different ways users ask questions (like “fees”, “cost”, “price”)
* 📝 Captures user contact details for follow-up

## Tech Used
* Python
* Streamlit
* Pandas

## How It Works

1. User types a message
2. The system understands the intent
3. It matches keywords with course data
4. Responds with relevant information

## Project Structure

app.py                 → Main app (UI + logic)
utils/
   intent.py           → Understands user queries
   recommender.py      → Fetches course details
   lead_manager.py     → Stores user info
course_data.csv        → Course dataset

## How to Run

1. Clone the repo:
git clone https://github.com/erinroseantony/ai-enquiry-assistant.git
2. Go into the folder:
cd ai-enquiry-assistant
3. Create virtual environment:
python -m venv venv
venv\Scripts\activate
4. Install requirements:
pip install -r requirements.txt
5. Run the app:
streamlit run app.py

## Demo

This app demonstrates:
* Course enquiry handling
* Fee-related queries
* Lead capture
* 
## Real-World Use

This can easily be extended to real applications by connecting it to WhatsApp using APIs like Twilio.

## About Me

**Erin Rose Antony**
Aspiring AI/ML Engineer 

## Final Thoughts

This project focuses on keeping things simple, practical, and user-friendly—just like real-world AI assistants.
Thanks for checking it out
