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


class ProductListView(ListView):
    model = Product
    template_name = 'shop-list.html'
    paginate_by = 10
    context_object_name = 'product_list'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def get_queryset(self):
        qs = self.model.objects.all()
        if self.kwargs.get('slug'):
            qs = qs.filter(tags__name=self.kwargs('slug'))
        return qs


