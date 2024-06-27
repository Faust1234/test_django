# catalog/urls.py

from django.urls import path
from .views import product_catalog, ProductListAPIView

urlpatterns = [
    path('catalog/', product_catalog, name='product_catalog'),
    path('api/products/', ProductListAPIView.as_view(), name='product_list_api'),
]
