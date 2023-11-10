from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'Title': 'BigHouzzz',
        'Header1': 'Главная страница!',
    }
    return render(request, 'core/index.html', context)

def about(request):
    return render(request, 'core/about.html')

def contacts(request):
    return render(request, 'core/contacts.html')