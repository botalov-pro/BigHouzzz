from django.shortcuts import render, get_object_or_404
from .models import Vehicle


def cars_index(request):
    """ Список транспортных средств """
    num_vehicles = Vehicle.objects.count()
    vehicles = Vehicle.objects.all()
    context = {
        'num_vehicles': num_vehicles,
        'vehicles': vehicles,
    }
    return render(request, 'cars/index.html', context)

def car_detail(request, car_id):
    """ Транспортное средство детально """
    vehicle = get_object_or_404(Vehicle, pk=car_id)
    context = {
        'vehicle': vehicle,
    }
    return render(request, 'cars/car_detail.html', context)
