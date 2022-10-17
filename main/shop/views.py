from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User, Group


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contact.html')


def product_view(request):
    return render(request, 'single-product.html')
