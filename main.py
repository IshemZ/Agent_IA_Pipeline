import requests

hackernews_ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").json()
#print(hackernews_ids)

keywords = ["AI", "Tech", "Data", "prompt"]

for article_id in hackernews_ids[:20]:
    article = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{article_id}.json?print=pretty").json()
    id = article['id']
    type = article['type']
    title = article['title']
    #text = article['text']
    
    
    #Si l'article contient un des mots clés, l'afficher
    if any(keyword.lower() in title.lower() for keyword in keywords):
            print(f"Title: {article['title']}")
            print(f"URL: {article['url']}")
            print("-" * 80)