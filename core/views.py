from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # FIXME: удалить return HttpResponse('<h1>Главная страница</h1>')
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contacts(request):
    return render(request, 'core/contacts.html')