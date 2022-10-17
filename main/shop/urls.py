from django.urls import path

from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/',views.contacts, name='contact'),
    path('single-product/', views.product_view, name='product')
]