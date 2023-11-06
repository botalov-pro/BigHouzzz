from django.shortcuts import render

def cars_index(request):
    return render(request, 'cars/index.html')