import requests

NEWS_API_KEY = "849c6632c40a43948acdc99f96112c2b"
NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_transfer_news(query="football transfer", page_size=10):
    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        return response.json().get("articles", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []
