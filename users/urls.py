from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.users_login, name='users_login'),
    path('signup/', views.users_signup, name='users_signup'),
]