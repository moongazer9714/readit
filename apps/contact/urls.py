from django.urls import path
from .views import contat_view
app_name = "contacts"

urlpatterns = [
    path('', contat_view, name='contact')
]
