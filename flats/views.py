from django.shortcuts import render

def flats_index(request):
    return render(request, 'cars/index.html') # FIXME: Исправить на страницу с flats