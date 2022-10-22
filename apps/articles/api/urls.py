from django.urls import path
from .views import article_list, article_create

urlpatterns = [
    path('list/', article_list),
    path('create/', article_create),
]