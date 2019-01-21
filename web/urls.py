

from django.urls import path

from web import views

urlpatterns = [
    path('index/', views.index, name='web'),
    path('share/', views.share, name='share'),
    path('list/', views.list, name='list'),
    path('about/', views.about, name='about'),
]