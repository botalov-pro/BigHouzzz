from django.shortcuts import render
from django.http import HttpResponse

def cars_index(request):
    # FIXME: удалить return HttpResponse('<h1>Машинки!</h1>')
    return render(request, 'cars/index.html')