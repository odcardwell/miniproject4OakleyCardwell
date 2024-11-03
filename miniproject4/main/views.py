# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Mini Project 4

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .models import Service, About, Project

def home(request):
    return render(request, 'main/home.html')

def about(request):
    about_content = About.objects.first()
    return render(request, 'main/about.html', {'about': about_content})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def services(request):
    services_list = Service.objects.all()
    return render(request, 'main/services.html', {'services': services_list})

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'main/portfolio.html', {'projects': projects})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')



