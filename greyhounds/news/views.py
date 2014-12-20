from django.http import HttpResponse
from django.shortcuts import render

from news import News

def index(request):
    news_items = News.objects.all()
    context = {"news": news_items}
    return render(request, "news/index.html", context)