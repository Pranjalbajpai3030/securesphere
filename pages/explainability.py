import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()
GENAI_API_KEY = st.secrets["GEMINIKEY"]  # Use Streamlit secrets for API key
if not GENAI_API_KEY:
    st.error("API Key not found. Set GEMINIKEY in .env file.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def explain_ai_decision(case_description):
    """Uses Gemini AI to explain cybersecurity decisions."""
    prompt = f"""
    You are an expert in AI Explainability and Cybersecurity. Analyze the following AI decision and explain:
    - How the AI arrived at this decision.
    - Whether any biases were involved.
    - The transparency of the decision-making process.
    - Ways to improve fairness and accuracy in future AI decisions.

    AI Decision Context:
    {case_description}

    Provide a clear, structured, and easy-to-understand explanation.
    """

    try:
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "No valid response received."
    except Exception as e:
        return f"Error: {str(e)}"

def show():
    st.title("🧠 Bias-free & Explainable AI")
    st.markdown("Understanding AI's decisions in cybersecurity.")

    # Sample AI decision scenarios
    sample_cases = {
        "Phishing Email Detection": "The AI flagged an email as phishing due to suspicious sender details and embedded malicious links.",
        "Intrusion Detection System (IDS) Alert": "The AI detected an unauthorized login attempt and classified it as a brute-force attack.",
        "Firewall Rule Automation": "The AI automatically blocked an IP address due to abnormal packet transmission patterns."
    }

    # Dropdown for sample AI decisions
    selected_case = st.selectbox("🔍 Select an AI decision to explain:", list(sample_cases.keys()))

    # Text area for custom input
    user_input = st.text_area("Or enter a custom AI decision for analysis:", sample_cases[selected_case])

    if st.button("Explain AI Decision"):
        with st.spinner("Analyzing AI decision..."):
            explanation = explain_ai_decision(user_input)
        
        st.subheader("💡 AI Explanation:")
        st.write(explanation)

if __name__ == "__main__":
    show()
