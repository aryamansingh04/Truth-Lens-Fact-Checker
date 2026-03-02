import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(query):
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "sortBy": "relevancy",
        "language": "en",
        "pageSize": 15,
        "searchIn": "title,description,content",
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "ok":
        print("Error fetching news:", data)
        return []

    return data.get("articles", [])