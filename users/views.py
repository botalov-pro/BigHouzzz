from django.shortcuts import render
def users_login(request):
    return render(request, 'users/login.html')

def users_signup(request):
    return render(request, 'users/signup.html')