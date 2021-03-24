from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    news = News.objects.all()
    context = {
        'news':  news,
        'title': 'List of news'
    }
    return render(request, 'news/index.html',
                  context=context)


def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')
