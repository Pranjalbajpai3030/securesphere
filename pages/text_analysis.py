import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GENAI_API_KEY = st.secrets["GEMINIKEY"]

if not GENAI_API_KEY:
    st.error("❌ API Key not found. Set GEMINIKEY in Streamlit Secrets.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Sample security logs
SAMPLE_LOGS = {
    "Firewall Alert": """🚨 **[Firewall] Unauthorized Access Attempt**  
**Threat Level:** High  
**Blocked Attempts:** 15 failed login attempts within 30 seconds  
**Action Taken:** IP temporarily blacklisted for 24 hours  
**Recommendation:** Enable SSH key-based authentication, use fail2ban, restrict access to trusted IPs.""" ,

    "Phishing Email Log": """✉️ **[Email Security] Suspicious Email Detected**  
**Sender:** hacker@example.com  
**Subject:** "Urgent! Reset Your Password"  
**Threat Level:** Critical  
**Indicators:** Suspicious domain, urgent language, fake branding  
**Action Taken:** Email quarantined, sender flagged  
**Recommendation:** Educate users on phishing awareness, enable advanced email filtering, enforce MFA.""" ,

    "Malware Detection": """🦠 **[Antivirus] Malicious File Detected**  
**File:** trojan.exe  
**Threat Level:** Severe  
**Behavior:** Attempts to encrypt files and connect to a C2 server  
**Action Taken:** File quarantined, network connection blocked  
**Recommendation:** Isolate infected system, update security patches, enable application whitelisting.""" 
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
        return f"❌ Error: {str(e)}"

def show():
    st.markdown("<h1 style='text-align: center; color: #3498db;'>📄 Text-based Security Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Upload security logs, paste logs, or use sample logs for AI-driven analysis.</p>", unsafe_allow_html=True)
    
    # Dropdown for sample logs
    sample_choice = st.selectbox("🔽 **Choose a sample security log (Optional)**", ["None"] + list(SAMPLE_LOGS.keys()))

    # Text area for user input
    text_input = st.text_area("📜 **Enter security log text**", value=SAMPLE_LOGS[sample_choice] if sample_choice != "None" else "", height=200)

    # Analyze Button
    if st.button("🚀 Analyze Logs"):
        if text_input.strip():
            analysis_result = analyze_logs_with_gemini(text_input)

            # Display Analysis Results in a Scrollable Box with Black Text
            st.markdown(f"""
                <div style="
                    background-color: #2d2d30; 
                    padding: 15px; 
                    border-radius: 10px; 
                    border: 2px solid #3498db;
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                    max-height: 400px; 
                    overflow-y: auto;
                    white-space: pre-wrap;
                    color: white;
                    font-family: monospace;
                ">
                    <h3 style="color: #ffffff;">🔍 Analysis Result:</h3>
                    <p style="color: white;">{analysis_result}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter some log data for analysis.")

if __name__ == "__main__":
    show()
