import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ---------------- LOAD ENV ----------------
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

# ---------------- USER PROFILE (UNIQUE PART) ----------------
user_profile = {
    "name": "Mallikjan Talikoti",
    "education": "BE Computer Science and Engineering",
    "college": "REC College, Hulkoti",
    "goal": "Become a Data Scientist and Civil Servant",
    "skills": ["Python", "Data Science", "Machine Learning", "Flask", "Streamlit"],
    "projects": ["Mini Bhindi AI"],
    "experience_level": "Student"
}

# ---------------- STREAMLIT PAGE ----------------
st.set_page_config(page_title="Mini Bhindi AI", page_icon="🥒", layout="centered")

st.title("🥒 Mini Bhindi AI")
st.caption("Your Personalized Real-Time AI Mentor")

# ---------------- SESSION MEMORY ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- MODEL ----------------
model = genai.GenerativeModel("gemini-1.0-pro")



# ---------------- SYSTEM PROMPT ----------------
system_prompt = f"""
You are Mini Bhindi AI, a personalized AI mentor.

User Details:
Name: {user_profile['name']}
Education: {user_profile['education']}
College: {user_profile['college']}
Career Goal: {user_profile['goal']}
Skills: {', '.join(user_profile['skills'])}
Experience Level: {user_profile['experience_level']}

Rules:
- Speak friendly and motivating
- Give personalized answers
- Suggest real-world projects
- Help in career, skills, resume, and learning
- NEVER say you don't know the user
- Act like a mentor, not a generic chatbot
"""

# ---------------- DISPLAY CHAT ----------------
for role, message in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Show user message
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append(("user", user_input))

    try:
        response = model.generate_content(
            system_prompt + "\nUser Question: " + user_input
        )

        ai_reply = response.text

    except Exception as e:
        ai_reply = f"⚠️ Error: {e}"

    # Show AI response
    st.chat_message("assistant").write(ai_reply)
    st.session_state.chat_history.append(("assistant", ai_reply))
