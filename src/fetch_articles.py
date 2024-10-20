import requests

def fetch_articles(query):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'apiKey': '9c338380989e43fe94899d094821fdf6',
        'language': 'en',
        'domains': 'thehindu.com,indiatimes.com,ndtv.com,indianexpress.com'
    }
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])
    return articles
