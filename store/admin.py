from django.contrib import admin
from . import models 
@admin.register(models.Product)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Product_name',)}
    list_display = ('Product_name','slug','stock','Category','modified_date','is_available')
    
@admin.register(models.Brand)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('brand_name',)}
    list_display = ('brand_name','slug')