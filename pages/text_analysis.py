import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()
GENAI_API_KEY = st.secrets["GEMINIKEY"]

if not GENAI_API_KEY:
    st.error("API Key not found. Set GEMINIKEY in Streamlit Secrets.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Sample security logs
SAMPLE_LOGS = {
    "Firewall Alert": """[Firewall] Blocked unauthorized access attempt from IP: 192.168.1.10  
    Possible brute-force attack detected on SSH port 22.  
    - Threat Level: High  
    - Blocked Attempts: 15 failed login attempts within 30 seconds  
    - Action Taken: IP temporarily blacklisted for 24 hours  
    - Recommendation: Enable SSH key-based authentication, use fail2ban, and restrict access to trusted IPs only."""  ,

"Phishing Email Log": """[Email Security] Suspicious email detected from sender: hacker@example.com  
    Subject: "Urgent! Reset Your Password"  
    Contains phishing link: http://malicious-site.com  
    - Threat Level: Critical  
    - Indicators: Suspicious domain, urgent language, fake branding  
    - Action Taken: Email quarantined, sender flagged  
    - Recommendation: Educate users on phishing awareness, enable advanced email filtering, enforce multi-factor authentication."""  ,

"Malware Detection": """[Antivirus] Detected malicious file: trojan.exe  
    Quarantined file located at: C:/Users/Admin/Downloads/trojan.exe  
    - Threat Level: Severe  
    - Behavior: Attempts to encrypt files and connect to a C2 server  
    - Action Taken: File quarantined, network connection blocked  
    - Recommendation: Isolate infected system, check for lateral movement, update security patches, enable application whitelisting."""  

}

def analyze_logs_with_gemini(log_text):
    prompt = f"""
    You are a cybersecurity expert. Analyze the following security logs and provide:
    - A summary of potential threats and vulnerabilities found.
    - Recommendations for security measures to mitigate risks.
    
    Logs:
    {log_text}
    """

    try:
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "No valid response received."
    except Exception as e:
        return f"Error: {str(e)}"

def show():
    st.title("📄 Text-based Security Analysis")
    st.markdown("Upload text files, paste logs, or use sample logs for analysis.")

    # Dropdown for sample logs
    sample_choice = st.selectbox("🔽 Choose a sample security log (Optional)", ["None"] + list(SAMPLE_LOGS.keys()))
    
    # Text area for user input
    text_input = st.text_area("Enter security log text", value=SAMPLE_LOGS[sample_choice] if sample_choice != "None" else "")

    if st.button("Analyze"):
        if text_input.strip():
            analysis_result = analyze_logs_with_gemini(text_input)
            st.subheader("🔍 Analysis Result:")
            st.write(analysis_result)
        else:
            st.warning("Please enter some log data for analysis.")

if _name_ == "_main_":
    show()