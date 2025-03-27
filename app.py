import streamlit as st
from components.sidebar import load_sidebar
from pages import home, text_analysis, image_analysis, conversational_ai, explainability, cyber_news

# Sidebar Navigation
PAGES = {
    "🏠 Home": home,
    "📄 Text Analysis": text_analysis,
    "🖼️ Image Analysis": image_analysis,
    "🤖 Conversational AI": conversational_ai,
    "🧠 Explainability": explainability,
    "🌐 Cyber News": cyber_news,
}

def main():
    st.set_page_config(page_title="Cybersecurity Dashboard", layout="wide")
    load_sidebar(PAGES)  # Load sidebar

if __name__ == "__main__":
    main()
