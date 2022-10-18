from django.urls import path

from shop import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product/<slug:brand_slug>/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('<slug:brand_slug>', views.ProductListView.as_view(), name='shop_brand')
]
