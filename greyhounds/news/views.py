from django.http import HttpResponse
from django.shortcuts import render

import news

def index(request):
    
    tags = request.GET.get("tags", "")
    tags = tags.split(",")
    if tags:
        news_items = news.News.objects.filter(tags__name__in=tags)
    else:
        news_items = news.News.objects.all()
        
    context = {"news": news_items}
    return render(request, "news/index.html", context)