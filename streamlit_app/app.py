import streamlit as st
from chatbot_model import get_bot_response

st.set_page_config(page_title="DigiBot - Marketing Chatbot", layout="centered")

st.title("🤖 DigiBot - Digital Marketing Chatbot")
st.markdown("Welcome! Ask me anything about marketing, pricing, services, etc.")

# Chat interaction
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", placeholder="Type your message...")

if st.button("Send") or user_input:
    if user_input:
        response = get_bot_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("DigiBot", response))

# Display chat history
for speaker, msg in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 DigiBot:** {msg}")

