import streamlit as st
from PIL import Image

def show():
    # Background Image
    st.markdown(
        """
        <style>
        .stApp {
            background: url("assets/logo.jpeg") no-repeat center center fixed;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # Hero Section
    st.markdown(
        """
        <div style='text-align: center; padding: 40px 0;'>
            <h1 style='color: #3498db;'>🔐 SecureSphere</h1>
            <h4>"Empowering Cybersecurity with AI"</h4>
        </div>
        """, 
        unsafe_allow_html=True
    )


    # Introduction (Centered)
    st.markdown(
        """
        <div style='text-align: center;'>
            <h3>🚀 Welcome to the SecureSphere Dashboard</h3>
            <p>This platform helps in analyzing cybersecurity threats using AI-powered models.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Features Section
    st.markdown("## 🔥 Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🛡️ Threat Detection")
        st.write("Identify and mitigate potential cybersecurity threats in real-time.")

    with col2:
        st.markdown("### 📊 Data Analytics")
        st.write("Gain insights into cyber threats through AI-driven analytics and reports.")

    with col3:
        st.markdown("### 🤖 AI-Powered Defense")
        st.write("Utilize machine learning models for automated threat analysis.")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("### 🔍 Explainability")
        st.write("Understand AI-driven decisions with transparency and clarity.")

    with col5:
        st.markdown("### 📰 Cyber News")
        st.write("Stay updated with the latest cybersecurity trends and threats.")

    with col6:
        st.markdown("### 📜 Reports & Logs")
        st.write("Access detailed reports and logs of previous threat analyses.")

    # Footer
    st.markdown(
        """
        <div style='text-align: center; margin-top: 50px;'>
            <h5 style='color: #777;'>Stay secure, stay ahead! 🔐</h5>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    show()
