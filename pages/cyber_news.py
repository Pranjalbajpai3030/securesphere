import streamlit as st
import requests

# NewsAPI credentials
API_KEY = "7c7c798ba157455299775fe83f2d8725"
NEWS_URL = "https://newsapi.org/v2/everything"

def fetch_cybersecurity_news():
    """Fetch latest cybersecurity-related news from NewsAPI."""
    params = {
        "q": "cybersecurity",  # Only fetch cyber-related news
        "apiKey": API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
    }

    response = requests.get(NEWS_URL, params=params)
    
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        return []

def show():
    # Page Title
    st.markdown(
        "<h1 style='text-align: center; color: #3498db;'>🌐 Cybersecurity News</h1>", 
        unsafe_allow_html=True
    )

    st.markdown("<h4 style='text-align: center;'>Get the latest cybersecurity updates!</h4>", unsafe_allow_html=True)

    # Button to Fetch News
    if st.button("Fetch Latest News 🔄"):
        news_articles = fetch_cybersecurity_news()

        if news_articles:
            st.markdown("<h2 style='text-align: center;'>📰 Latest Cyber News</h2>", unsafe_allow_html=True)

            for article in news_articles[:10]:  # Show top 10 articles
                # News Card Layout
                st.markdown(
                    f"""
                    <div style="
                        background-color: #f8f9fa;
                        border-radius: 12px;
                        padding: 20px;
                        margin: 10px 0;
                        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                        display: flex;
                        flex-direction: row;
                        align-items: center;
                        width: 100%;
                    ">
                        <div style="flex: 1;">
                            <h3 style="color: #2c3e50;">{article['title']}</h3>
                            <p>{article['description']}</p>
                            <a href="{article['url']}" target="_blank" style="
                                display: inline-block;
                                padding: 10px 15px;
                                margin-top: 10px;
                                text-decoration: none;
                                background-color: #3498db;
                                color: white;
                                border-radius: 5px;
                            ">🔗 Read More</a>
                        </div>
                        <div>
                            <img src="{article['urlToImage']}" width="200" style="border-radius: 8px; margin-left: 20px;" />
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.warning("⚠️ No cybersecurity news found!")

if __name__ == "__main__":
<<<<<<< HEAD
    show()
=======
    show()
>>>>>>> 44bbffab3baa539e012573a4889935a75e8691ea
