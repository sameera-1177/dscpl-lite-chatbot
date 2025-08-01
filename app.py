import streamlit as st
import requests

st.set_page_config(page_title="DSCPL Lite – Your Spiritual AI Chatbot", layout="centered")

st.title("🙏 DSCPL Lite – Spiritual Chat Companion")
st.write("Welcome! Share your thoughts or select a mood for faith-based encouragement.")

# Mood selector
mood = st.selectbox("How are you feeling today?", ["Select", "Anxious", "Grateful", "Lonely", "Hopeful", "Lost"])

# Input box
user_input = st.text_input("Ask me anything spiritual, or share how you feel:")

# OpenRouter API
import streamlit as st

api_key = st.secrets["OPENROUTER_API_KEY"]

def get_response(prompt):
    headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://sameera-1177.streamlit.app",  
}

    json_data = {
        "model": "mistralai/mistral-7b-instruct",  # You can try "openai/gpt-3.5-turbo" if this fails
        "messages": [{"role": "user", "content": prompt}],
    }
    
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data)
        data = response.json()
        
        # Check if response contains choices
        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            st.error("⚠️ OpenRouter error: " + data.get("error", {}).get("message", "No valid response"))
            return "🙏 Sorry, I couldn't reach the spiritual realm. Try again!"
    
    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")
        return "🛑 Something went wrong. Please check your API key or prompt."


if st.button("Speak to DSCPL"):
    if mood != "Select":
        prompt = f"I am feeling {mood.lower()}. Give me a Bible-based, peaceful message."
    elif user_input:
        prompt = user_input
    else:
        prompt = "Give me a spiritual encouragement for today."

    with st.spinner("Thinking holy thoughts..."):
        reply = get_response(prompt)
        st.success(reply)
