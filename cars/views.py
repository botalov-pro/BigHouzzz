from django.shortcuts import render
from django.http import HttpResponse

def cars_index(request):
    return HttpResponse('<h1>Машинки!</h1>')