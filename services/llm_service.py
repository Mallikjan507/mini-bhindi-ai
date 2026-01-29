import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load env
load_dotenv()

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 🔍 Find a working model dynamically
def get_working_model():
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            return genai.GenerativeModel(m.name)
    return None


model = get_working_model()


def get_response(user_input: str) -> str:
    if model is None:
        return "❌ No Gemini models available for this API key. Please enable Gemini API in Google AI Studio."

    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini API Error: {e}"
