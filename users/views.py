from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
from .forms import CustomUserCreationForm
from .utils import paginateObjects, searchProfiles
from django.db.models import Q

def landing(request):
    if request.usery.is_authenticated:
        return redirect('profiles')
    profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateObjects(request, 
        profiles, 3)
    context = {'profiles': profiles, 
    'search_query': search_query,
    'custom_range': custom_range}

    return render(request, 'landing.html', context)


def landingLogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 
                'Такого пользователя нет в системе')
        user = authenticate(request, username=username, 
            password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' 
                in request.GET else 'account')
        else:
            messages.error(request, 
                'Неверное имя пользователя или пароль')
    return redirect('landing')

def profiles(request):
    profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateObjects(request, 
        profiles, 3)
    context = {'profiles': profiles, 
    'search_query': search_query,
    'custom_range': custom_range}
    return render(request, 'users/profiles.html', context)

def loginUser(request):

    if request.usery.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 
                'Такого пользователя нет в системе')

        user = authenticate(request, 
            username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' 
                in request.GET else 'account')

        else:
            messages.error(request, 
                'Неверное имя пользователя или пароль')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'Вы вышли из учетной записи')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 
                'Аккаунт успешно создан!')

            login(request, user)
            return redirect('edit-account')

        else:
            messages.success(request, 
                'Во время регистрации возникла ошибка')

    context = {'page': page, 'form': form}
    return render(request, 
        'users/login_register.html', context)



