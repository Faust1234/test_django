# catalog/models.py

from django.db import models
from django.utils.text import slugify
import sys


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    url = models.URLField(max_length=255, null=True)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='product_previews/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.url:
            self.url = f"http://localhost:8000/api/products/?search={self.name}/"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    product = models.ManyToManyField(Product)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
