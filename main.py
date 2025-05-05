import requests
import json
from datetime import datetime
import os
print(os.getcwd())
print(os.access(".", os.W_OK))

hackernews_ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").json()
#print(hackernews_ids)

keywords = ["AI", "Tech", "Data", "prompt"]

#json file path
file_path = "/api_call.json"

#Chargement des article déjà stockés s'il y en a
try:
    with open(file_path, "r") as f:
        saved_articles = json.load(f)
except FileNotFoundError :
    saved_articles = []

#Stocker les nouveaux articles
for article_id in hackernews_ids[:20]:
    article = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{article_id}.json?print=pretty").json()
    #id = article['id']
    #type = article['type']
    title = article['title']
    #text = article['text']
    
    
    #Si l'article contient un des mots clés, l'afficher
    if any(keyword.lower() in title.lower() for keyword in keywords):
            filtered_article = {
            "id": article.get("id"),
            "type": article.get("type"),
            "title": title,
            "url": article.get("url"),
            "timestamp": datetime.utcnow().isoformat()
            }
            
            print(f"Title: {title}")
            print(f"URL: {article.get('url')}")
            print("-" * 80)
            
            if not any(a["id"] == filtered_article["id"] for a in saved_articles):
                saved_articles.append(filtered_article)
                
#Sauvegarde du json
with open(file_path, "w") as f:
    json.dump(saved_articles, f, indent=4)
