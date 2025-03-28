import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import os
import io

# Load environment variables
load_dotenv()
GENAI_API_KEY = os.getenv("GEMINIKEY")

if not GENAI_API_KEY:
    st.error("❌ API Key not found. Set GEMINIKEY in .env file.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

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
        return f"❌ Error: {str(e)}"

def show():
    # Cool Header with Centered Title
    st.markdown("""
        <div style="text-align: center;">
            <h1 style="color: #3498db;">🖼️ Image-based Security Analysis</h1>
            <p style="font-size: 16px;">Upload an image (email screenshot, system logs, or suspicious files) for security analysis.</p>
        </div>
    """, unsafe_allow_html=True)

    # File Upload Section
    uploaded_file = st.file_uploader("📂 **Upload an Image (PNG, JPG, JPEG)**", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Display Uploaded Image Centered
        st.markdown("<h3 style='text-align: center;'>📷 Uploaded Image</h3>", unsafe_allow_html=True)
        st.image(uploaded_file, caption="Preview", use_column_width=True)

        # Analyze Button with Spinner
        if st.button("🚀 Analyze Image"):
            with st.spinner("🔍 Analyzing... Please wait"):
                image_bytes = io.BytesIO()
                img = Image.open(uploaded_file)
                img.save(image_bytes, format="PNG")  # Convert image to bytes
                analysis_result = analyze_image_with_gemini(image_bytes)

            # Display Analysis Result in a Scrollable Styled Box
            st.markdown("""
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
                    <p style="color: white;">{}</p>
                </div>
            """.format(analysis_result), unsafe_allow_html=True)

if __name__ == "__main__":
    show()
