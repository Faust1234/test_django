# catalog/admin.py

from django.contrib import admin
from .models import Product, Attribute

admin.site.register(Product)
admin.site.register(Attribute)
