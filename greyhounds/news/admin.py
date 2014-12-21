from django.contrib import admin
import news

admin.site.register(news.News)
admin.site.register(news.Tag)