
import requests
from config import NEWS_API_KEY

def get_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey=" + NEWS_API_KEY
    response = requests.get(url)
    return response.json()
