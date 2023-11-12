from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.users_login, name='users_login'),
    path('signup/', views.users_signup, name='users_signup'),
]