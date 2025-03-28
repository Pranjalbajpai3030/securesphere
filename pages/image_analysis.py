import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import io
import os
import base64

# Load environment variables
load_dotenv()
GENAI_API_KEY = st.secrets["GEMINIKEY"]

if not GENAI_API_KEY:
    st.error("API Key not found. Set GEMINIKEY in Streamlit Secrets.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Sample images (Base64 encoded placeholders)
SAMPLE_IMAGES = {
    "Phishing Email Screenshot": "./assets/sample_phishing.png",
    "Malware Alert Screenshot": "./assets/sample_malware.png",
    "Suspicious System Logs": "./assets/sample_logs.png"
}

def analyze_image_with_gemini(image_bytes):
    """ Sends image to Gemini API for security analysis. """
    prompt = """
    You are a cybersecurity expert. Analyze the uploaded image and determine:
    - Whether it contains a phishing email, malicious content, or a security threat.
    - If the image is an email screenshot, check for phishing indicators like:
      - Suspicious sender address
      - Fake links (typosquatting, shortened URLs)
      - Urgent language or scare tactics
      - Mismatched branding/logos
      - Request for sensitive information
    - If the image is a system screenshot, check for visible security vulnerabilities.
    - Provide recommendations for security measures if threats are detected.
    """

    try:
        image_part = {"mime_type": "image/png", "data": image_bytes.getvalue()}
        response = model.generate_content([prompt, image_part])
        return response.text if hasattr(response, "text") else "No valid response received."
    except Exception as e:
        return f"Error: {str(e)}"

def show():
    st.title("🖼 Image-based Security Analysis")
    st.markdown("Upload an image (email screenshot, system logs, or suspicious file) for security analysis.")

    # Dropdown for sample images
    sample_choice = st.selectbox("🔽 Choose a sample security image (Optional)", ["None"] + list(SAMPLE_IMAGES.keys()))

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    # Load sample image if selected
    if sample_choice != "None":
        image_path = SAMPLE_IMAGES[sample_choice]
        uploaded_file = open(image_path, "rb")

    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Image"):
            with st.spinner("Analyzing..."):
                image_bytes = io.BytesIO()
                img.save(image_bytes, format="PNG")  # Convert image to bytes
                analysis_result = analyze_image_with_gemini(image_bytes)
                
            st.subheader("🔍 Analysis Result:")
            st.write(analysis_result)

if _name_ == "_main_":
    show()