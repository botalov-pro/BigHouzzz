from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from users.forms import UserLoginForm

def login(request):
    if request.method == 'POST':  # Если POST-запрос на получение данных с формы
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:  # Если пользователь прошел атентификацию и активный, то
                auth.login(request, user)  # авторизовать
                return HttpResponseRedirect('/') # и перенаправить на Главную  # FIXME: Переделать с использованием reverse('index') вместо '/'
    else:  # Если не POST-запрос, то
        login_form = UserLoginForm()
    context = {
        'form': login_form
    }
    return render(request, 'users/login.html', context)

def signup(request):
    return render(request, 'users/signup.html')