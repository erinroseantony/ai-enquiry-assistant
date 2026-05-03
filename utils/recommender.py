import pandas as pd

df = pd.read_csv("course_data.csv")

def recommend_course(message):
    message = message.lower()
    words = message.split()

    for _, row in df.iterrows():
        keywords = str(row["keyword"]).lower().split(",")

        for keyword in keywords:
            keyword = keyword.strip()

            # ✅ exact word match (fixes "ai" in "available")
            if keyword in words:
                return f"""
📘 Course: {row['course_name']}
⏳ Duration: {row['duration']}
💰 Fees: {row['fees']}
👉 Please share your contact details to proceed!
"""

    return None