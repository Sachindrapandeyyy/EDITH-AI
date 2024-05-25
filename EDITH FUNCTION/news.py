import json
import requests

url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=b6975815cc3d4eaa9fa34d5c46f921a0'

def news():
    req = requests.get(url)
    news = json.loads(req.text)
    
    formatted_news =[]
    for i, article in enumerate(news["articles"][:10],start=1):
        formatted_article = f"{i}.{article['title']}\n{article['description']}\n"
        formatted_news.append(formatted_article)
    return formatted_news    
    
news()
