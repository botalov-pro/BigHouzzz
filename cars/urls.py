from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.cars_index, name='cars_index'),
]
