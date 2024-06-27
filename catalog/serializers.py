# catalog/serializers.py

from rest_framework import serializers
from .models import Product, Attribute


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'url', 'description', 'preview_image']


class AttributeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Attribute
        fields = ['name', 'slug', 'products']
