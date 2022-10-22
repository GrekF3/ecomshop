from django.urls import path
from .views import account, login


urlpatterns = [
    path('login/', login, name='login'),
    path('account/', account, name='account'),
]