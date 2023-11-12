from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.users_login, name='login'),
    path('signup/', views.users_signup, name='signup'),
]