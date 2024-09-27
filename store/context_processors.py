from .models import Brand

def brands_query(request):
    brands = Brand.objects.all()
    print(brands) 
    return {'brands': brands}