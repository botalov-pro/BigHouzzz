from django.shortcuts import render, get_object_or_404
from .models import Vehicle, VehicleCategory


def cars_index(request):
    """ Список транспортных средств """
    # Получение списка категорий транспортных средств
    list_cat = VehicleCategory.objects.filter(is_active=True).order_by('name')

    if request.method == "POST":
        selected_category = int(request.POST.get('category_filter'))
        if selected_category == 0:  # Не выбрана ни одна из категорий
            vehicles = Vehicle.objects.filter(is_active=True)
        else:
            vehicles = Vehicle.objects.filter(is_active=True,
                                              category=selected_category)
    else:  # Если это GET-запрос (впервые открывается страница)
        selected_category = 0
        vehicles = Vehicle.objects.filter(is_active=True)

    num_vehicles = vehicles.count()
    context = {
        'categories': list_cat,
        'selected_category': selected_category,
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
