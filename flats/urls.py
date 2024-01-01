from django.contrib import admin
from django.views.generic.base import TemplateView
from django.urls import path
from . import views

app_name = 'flats'

urlpatterns = [
    path('<int:house_id>/', views.house_detail, name='house_detail'),
    path('<int:house_id>/<int:room_id>/', views.room_detail, name='room_detail'),
    path('', views.rooms_index, name='rooms_index'),
]
