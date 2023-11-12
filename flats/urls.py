from django.contrib import admin
from django.views.generic.base import TemplateView
from django.urls import path
from . import views

app_name = 'flats'

urlpatterns = [
    path('', views.flats_index, name='flats_index'),
]