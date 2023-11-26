from django.shortcuts import render


def rooms_index(request):
    return render(request, 'rooms/rooms_index.html')


def houses_index(request):
    return render(request, 'rooms/houses_index.html')


def room_detail(request):
    return render(request, 'rooms/room_detail.html')


def house_detail(request):
    return render(request, 'rooms/house_detail.html')