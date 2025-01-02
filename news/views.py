from django.shortcuts import render, redirect
from django.utils import timezone  # Add this import
from datetime import datetime
import json

NEWS_JSON_PATH = '/home/jacky/PycharmProjects/HyperNews Portal/HyperNews Portal/task/hypernews/news.json'

def load_articles():
    with open(NEWS_JSON_PATH, 'r') as file:
        return json.load(file)
def save_articles(articles):
    with open(NEWS_JSON_PATH, 'w') as file:
        json.dump(articles, file, indent=4)

def news_list(request):
    articles = load_articles()
    for article in articles:
        # Convert the 'created' field to a date string for grouping
        article['created_date'] = datetime.strptime(article['created'], '%Y-%m-%d %H:%M:%S').date().isoformat()
    query = request.GET.get('q', '')
    if query:
        filtered_articles = [article for article in articles if query.lower() in article['title'].lower()]
    else:
        filtered_articles = articles
    return render(request, 'news_list.html', {'articles': filtered_articles})

def news_create(request):
    if request.method == 'POST':
        articles = load_articles()
        # Use 'link' as the unique identifier for articles
        max_link = max((article.get('link', 0) for article in articles), default=0)
        new_article = {
            'link': max_link + 1,
            'title': request.POST.get('title', '').strip(),
            'text': request.POST.get('text', '').strip(),
            'created': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        articles.append(new_article)
        save_articles(articles)
        return redirect('/news/')
    return render(request, 'news_create.html')

def news_detail(request, article_id):
    articles = load_articles()
    # Use 'link' instead of 'id' to find the article
    article = next((article for article in articles if article['link'] == article_id), None)
    if not article:
        return render(request, '404.html', status=404)  # Render a 404 page if article not found
    return render(request, 'news_detail.html', {'article': article})

def coming_soon(request):
    return redirect('/news/')