from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from users.forms import UserLoginForm, UserRegistrationForm

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
    if request.method == 'POST':  # Если POST-запрос на получение данных с формы
        registration_form = UserRegistrationForm(data=request.POST)
        if registration_form.is_valid():
            registration_form.save()  # Сохраняем форму
            return HttpResponseRedirect('/')  # Переадресация на страницу авторизации  # FIXME: Сделать перенаправление на страницу авторизации
    else:
        registration_form = UserRegistrationForm()
    context = {
        'form': registration_form
    }
    return render(request, 'users/signup.html', context)


def profile(request):
    if request.method == 'POST':  # Если POST-запрос на получение данных с формы
        profile_form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()  # Сохраняем форму
            return HttpResponseRedirect('/profile') # Переадресация на страницу авторизации  # FIXME: Сделать перенаправление с помощью reverse
    else:
        profile_form = UserProfileForm(instance=request.user)
    context = {
        'form': profile_form
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')  # перенаправить на Главную  # FIXME: Переделать с использованием reverse('index') вместо '/'
