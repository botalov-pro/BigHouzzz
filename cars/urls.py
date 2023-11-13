from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('<int:car_id>/', views.car_detail, name='car_detail'),
    path('', views.cars_index, name='cars_index'),
]
