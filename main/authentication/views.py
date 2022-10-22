from django.contrib import messages
from django.shortcuts import render, redirect
from authentication.forms import CustomUserCreationForm, UserLogin
from users.models import User
from django.contrib.auth import login, authenticate, logout


def account(request):

    user = request.user


    context = ({
        'user_full_name': user.get_full_name(),
        'user_name': user.get_short_name(),
        'user_last_name': user.get_last_name(),
        'user_country': user.get_country(),
        'user_state': user.get_state(),
        'user_city': user.get_city(),
        'user_phone': user.get_phone(),
    })


    return render(request, 'my-account.html', context)


def register_R(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()


def login_req(request):
    if request.method == "POST":
        form = UserLogin(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Успешный вход {username}")
                return redirect('account')
            else:
                messages.error(request, 'Неверный логин или пароль.')
        else:
            messages.error(request, 'Неверный логин или пароль.')

    form = UserLogin()
    return render(request=request, template_name='login.html', context={
        'form': form
    })

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
