from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.index, name='index'),
]
