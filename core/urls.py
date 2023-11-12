from django.contrib import admin
from django.views.generic.base import TemplateView
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('about/', views.AboutProjectView.as_view(), name='about'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('', views.index, name='index'),
]
