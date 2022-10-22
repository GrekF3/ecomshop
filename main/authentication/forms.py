from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from users.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'country', 'state', 'city', 'phone', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'country', 'state', 'city', 'phone', 'email')

class UserLogin(AuthenticationForm):

    class Meta:
        model = User
        fields = ('email', 'password')
