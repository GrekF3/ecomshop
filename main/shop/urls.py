from django.urls import path

from shop import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contacts, name='contact'),
    path('product/<slug:brand_slug>/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
