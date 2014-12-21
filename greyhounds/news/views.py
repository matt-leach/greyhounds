from django.http import HttpResponse
from django.shortcuts import render

import news

def index(request):
    
    
    try:
        tags = request.GET["tags"].split(",")
        news_items = news.News.objects.filter(tags__name__in=tags)
    except KeyError:
        news_items = news.News.objects.all()
        
    context = {"news": news_items}
    return render(request, "news/index.html", context)

