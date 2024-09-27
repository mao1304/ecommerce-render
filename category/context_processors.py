from .models import Category, Type

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def menu_2(request):
    types = Type.objects.all()
    print(types) 
    return {'types': types}
