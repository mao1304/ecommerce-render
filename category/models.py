from django.db import models
from django.urls import reverse

class Type(models.Model):
    Type_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Type_name
class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    tipe = models.ForeignKey(Type, on_delete=models.CASCADE)
    cat_image = models.ImageField(upload_to='images/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    
    def __str__(self):
        return self.category_name
    

    
    