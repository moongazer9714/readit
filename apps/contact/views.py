from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


# Create your views here.


def _contat_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('contacts:contact')
    context = {}
    return render(request, 'contact.html', context)


def contat_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact')
    context = {"form": form}
    return render(request, 'contact.html', context)
