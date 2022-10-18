from django.shortcuts import render
from .models import *
from django.views.generic import DetailView
from django.views.generic import ListView


def index(request):
    ads = Ad.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html', {'ads': ads,
                                          'products': products})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'






def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contact.html')
