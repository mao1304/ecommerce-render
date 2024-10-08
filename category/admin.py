from django.contrib import admin
from .models import Category, Type

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name','slug')
    pass
    
admin.site.register(Type) 
