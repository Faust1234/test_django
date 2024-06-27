# catalog/views.py

from rest_framework import generics
from django.http import HttpResponse
from django.template import loader
from rest_framework import filters
from .models import Product

from .serializers import ProductSerializer


def product_catalog(request):
    products = Product.objects.all()
    template = loader.get_template('catalog/catalog.html', using='jinja2')
    context = {'products': products}
    return HttpResponse(template.render(context, request))


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'url', 'description']
