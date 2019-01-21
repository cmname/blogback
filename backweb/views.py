from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from backweb.Artform import UserLoginForm, UserRegisterForm, AddArtForm, UpArtForm
from backweb.models import MyUser, Article


def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['userpwd']
            user = MyUser.objects.filter(username=username).first()
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('backweb:index'))
            else:
                ers = '账号或密码错误'
                return render(request, 'backweb/login.html', {'ers': ers})
        else:
            errors = form.errors
            return render(request, 'backweb/login.html', {'errors': errors})


def register(request):
    if request.method == 'GET':
        return render(request, 'backweb/register.html')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_password = make_password(password)
            MyUser.objects.create(username=username, password=new_password)
            return HttpResponseRedirect(reverse('backweb:login'))
        else:
            errors = form.errors
            return render(request, 'backweb/register.html', {'errors': errors})


def index(request):
    if request.method == 'GET':
        return render(request, 'backweb/index.html')


def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        paginator = Paginator(articles, 3)
        page = paginator.page(page)
        return render(request, 'backweb/article.html', {'page': page})


def category(request):
    if request.method == 'GET':
        return render(request, 'backweb/category.html')


def update_article(request,id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        return render(request, 'backweb/update_article.html', {'article': article})
    if request.method == 'POST':
        form = UpArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            describe = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            article = Article.objects.filter(pk=id).first()
            article.title = title
            article.desc = describe
            article.content = content
            if icon:
                article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            article = Article.objects.filter(pk=id).first()
            return render(request, 'backweb/article.html', {'article': article})


def add_article(request):
    if request.method == 'GET':
        return render(request, 'backweb/add_article.html')
    if request.method == 'POST':
        icon = request.FILES.get('icon')
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            Article.objects.create(title=title, desc=desc,
                                   content=content, icon=icon)
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            return render(request, 'backweb/add_article.html', {'form': form})


def del_article(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:article'))