from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q 

from carts.models import CartItem
from carts.views import _cart_id
from .models import Product
from category.models import Category 


# def store(request):
#     return render(request,'store/shop.html')

def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(Category=categories, is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
        
          
    context = {
        'products': paged_products,
        'products_count': product_count, 
        }
    return render(request,'store/shop.html', context)

def product_detail(request, category_slug, product_slug):
    
    try: 
        single_product = Product.objects.get(Category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product = single_product).exists()
    except Exception as e:
        raise e
    print(single_product.description)

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    print(single_product)
    return render(request,'store/shop-single.html', context)
    
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter( Q(description_icontains=keyword))