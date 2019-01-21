from django.shortcuts import render

from backweb.models import Article


def index(request):
    if request.method == 'GET':
        article = Article.objects.all()
        return render(request, 'web/index.html', {'article': article})


def share(request):
    if request.method == 'GET':
        article = Article.objects.all()
        return render(request, 'web/share.html', {'article': article})


def list(request):
    if request.method == 'GET':
        article = Article.objects.all()
        return render(request, 'web/list.html', {'article': article})


def about(request):
    if request.method == 'GET':
        article = Article.objects.all()
        return render(request, 'web/about.html', {'article': article})