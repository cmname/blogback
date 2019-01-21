
from django.urls import path

from backweb import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('article/', views.article, name='article'),
    path('category/', views.category, name='category'),
    path('update_article/<int:id>/', views.update_article, name='update_article'),
    path('add_article/', views.add_article, name='add_article'),
    path('del_article/', views.del_article, name='del_article'),
]