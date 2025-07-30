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
api_key = "PASTE-YOUR-OPENROUTER-API-KEY-HERE"

def get_response(prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://your-username.streamlit.app",  # optional, replace later
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data)
    return response.json()["choices"][0]["message"]["content"]

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
