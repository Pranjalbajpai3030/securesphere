import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()
GENAI_API_KEY = st.secrets["GEMINIKEY"]

if not GENAI_API_KEY:
    st.error("API Key not found. Set GEMINIKEY in .env file.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def get_ai_response(user_query):
    """Generates a chatbot response based on cybersecurity threats."""
    prompt = f"""
    You are an AI cybersecurity expert. Respond concisely and informatively to the user's query.
    Ensure responses are accurate, practical, and security-focused.

    User Query:
    {user_query}
    """

    try:
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "No valid response received."
    except Exception as e:
        return f"Error: {str(e)}"

def show():
    st.title("🤖 Conversational AI for Threat Insight")
    st.markdown("Chat with an AI cybersecurity expert about threats, vulnerabilities, and best practices.")

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User input field
    user_input = st.text_input("💬 Ask about cybersecurity threats:")

    if st.button("Get AI Response"):
        if user_input.strip():
            with st.spinner("Analyzing..."):
                ai_response = get_ai_response(user_input)
            
            # Save conversation to session history
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("AI", ai_response))
    
    # Display chat history
    st.subheader("🗨️ Chat History")
    for speaker, message in st.session_state.chat_history:
        st.markdown(f"**{speaker}:** {message}")

if __name__ == "__main__":
    show()
