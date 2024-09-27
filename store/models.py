from django.db import models
from django.urls import reverse
from category.models import Category

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    image = models.ImageField( upload_to='media/images/products')

    def __str__(self):
        return self.brand_name
class Product(models.Model):
    Product_name = models.CharField(max_length=200, unique = True)
    slug = models.CharField(max_length=200,unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='media/images/products')
    stock = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.Category.slug, self.slug])
    
    def get_urls(self):
        return reverse('product_by_brand', args=[self.brand.slug, self.slug])
    def __str__(self):
        return self.Product_name


