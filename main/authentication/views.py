from django.shortcuts import render, redirect
from authentication.forms import CustomUserCreationForm, UserLogin
from users.models import User


def account(request):

    context = ({
        'user': User
    })

    return render(request, 'my-account.html', context)


def register(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    elif request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            form.confirm_login_allowed(User)



def login(request):
    return render(request,'login.html')
