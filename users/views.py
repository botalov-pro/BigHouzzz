from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import auth, messages
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

def login(request):
    """ Вход пользователя """
    if request.method == 'POST':  # Если POST-запрос на получение данных с формы
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:  # Если пользователь прошел атентификацию и активный, то
                auth.login(request, user)  # авторизовать
                return redirect('core:index')  # перенаправить на Главную
    else:  # Если не POST-запрос, то
        login_form = UserLoginForm()
    context = {
        'form': login_form
    }
    return render(request, 'users/login.html', context)

def signup(request):
    """ Регистрация нового пользователя """
    if request.method == 'POST':  # Если POST-запрос на получение данных с формы
        registration_form = UserRegistrationForm(data=request.POST)
        if registration_form.is_valid():
            registration_form.save()  # Сохраняем форму
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('users:login')  # Переадресация на страницу авторизации
    else:
        registration_form = UserRegistrationForm()
    context = {
        'form': registration_form
    }
    return render(request, 'users/signup.html', context)


def profile(request):
    """ Профиль пользователя """
    if request.method == 'POST':  # Если POST-запрос на получение данных с формы
        profile_form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()  # Сохраняем форму
            return redirect('profile')  # Переадресация на страницу профиля
    else:  # Если не POST-запрос, то
        profile_form = UserProfileForm(instance=request.user)
    context = {
        'form': profile_form
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    """ Выход пользователя """
    auth.logout(request)
    return redirect('core:index')  # перенаправить на Главную
