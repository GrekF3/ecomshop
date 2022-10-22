from django.urls import path

from main import settings
from .views import account, login_req, logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('account/', account, name='account'),
    path('login/', login_req, name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
