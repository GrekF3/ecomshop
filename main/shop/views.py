from django.http import Http404
from django.shortcuts import render
from .models import *
from django.views.generic import DetailView
from django.views.generic import ListView


def index(request):
    ads = Ad.objects.all()
    products = Product.objects.all()
    brands = Brand.objects.all()

    popular_products = Product.objects.all().order_by('-rating')[:10]

    context = ({
        'ads':ads,
        'products':products,
        'brands':brands,
        'popular_products':popular_products,
    })

    return render(request, 'index.html', context=context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'shop-list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        qs = self.model.objects.all()
        if self.kwargs.get('brand_slug'):
            qs = qs.filter(brand__slug=self.kwargs['brand_slug'])
            check = list(qs)
            if not check:
                raise Http404
        return qs


def customhandler404(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response
