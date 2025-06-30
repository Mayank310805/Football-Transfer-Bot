import streamlit as st
from datetime import datetime
from news_fetcher import fetch_transfer_news
from summarizer import summarize_text

# === Helper ===
def format_date(iso_date):
    try:
        return datetime.fromisoformat(iso_date[:-1]).strftime("%d %b %Y, %I:%M %p")
    except:
        return iso_date

# === Streamlit App ===
def main():
    st.set_page_config(page_title="⚽ Football Transfer News Bot", layout="wide")
    st.title("⚽ Football Transfer Market News Bot")
    st.markdown("Stay updated with the latest **football transfer** stories, summarized for quick reading.")

    with st.sidebar:
        st.header("🔍 Filters")
        query = st.text_input("Search Topic", "football transfer")
        num_articles = st.slider("Number of Articles", 5, 20, 10)

    st.info(f"Fetching top {num_articles} news for: **{query}**")
    articles = fetch_transfer_news(query, num_articles)

    if not articles:
        st.warning("No articles found. Try a different search keyword.")
        return

    for i, article in enumerate(articles):
        with st.expander(f"📰 {article['title']}", expanded=False):
            st.write(f"**Source**: {article['source']['name']} | **Published on**: {format_date(article['publishedAt'])}")
            st.markdown(f"[Read Full Article]({article['url']})")

            if article.get("content"):
                summary = summarize_text(article["content"])
                st.write("**Summary:**")
                st.success(summary)
            else:
                st.warning("No content to summarize.")

if __name__ == "__main__":
    main()
    
