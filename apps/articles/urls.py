from django.urls import path
from .views import index, single_article, article, views_up

app_name = "articles"

urlpatterns = [
    path('', index, name='index'),
    path('blogs/', article, name='article'),
    path('views_up/<int:pk>/', views_up, name='views_up'),
    path('article/<int:pk>/', single_article, name='single-article'),
]
