from django.shortcuts import render, get_object_or_404
from .models import Vehicle


def cars_index(request):
    return render(request, 'cars/index.html')
def car_detail(request, car_id):
    vehicle = get_object_or_404(Vehicle, pk=car_id)
    context = {
        'vehicle': vehicle,
    }
    return render(request, 'cars/car_detail.html', context)
