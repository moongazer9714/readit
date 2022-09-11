from django.shortcuts import render
from .models import FeedBack
# Create your views here.


def about_view(request):
    happy_clients = FeedBack.objects.all()
    context = {"happy_clients": happy_clients}
    return render(request, 'about.html', context)
