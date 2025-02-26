from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from . models import Product
from category.models import Category
from carts.views import _cart_id
from carts.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.


def store(request, category_slug=None):
    
    categories = None 
    products = None 
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        # first decides the category and pass to the category 
        products = Product.objects.filter(category=categories, is_available=True) # fetching form database 
        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6) # passing the products and how many want on the one page Here paginator contain 8 items 
        page = request.GET.get('page') # here we getting from front by url page=2
        paged_products = paginator.get_page(page)  # here paged_products contains 6 products
        product_count = products.count() # here count is the python builtin method and we count the all product
        
    context = {
        'products': paged_products,
        'product_count': product_count, # making available to the store.html
        
    }
    return render(request, 'store/store.html', context)

# category_slug,product_slug


def product_detail(request, category_slug, product_slug):
    try:
        # Fetch product using category slug and product slug
        single_product = Product.objects.get(category__slug= category_slug, slug =product_slug) # here we matching category__slug to the url
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product = single_product).exists()# this is for if item is present in the cart or not

    except Exception as e:
        raise e 
        
    # Context dictionary to pass to the template
    context = {
        "single_product": single_product,
        "in_cart": in_cart,
    }

    # Render the template with the context
    return render(request, 'store/product_detail.html', context)

def search(request):
    
    if 'keyword' in request.GET: # checking if the get request contain word 'keyword'
        keyword = request.GET['keyword'] # if present fetching the value 
        
        if keyword:
            products = Product.objects.order_by('created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword)) # icontains search based on the keyword
            product_count = products.count() # showing the number on teh ui 
        context = {
            'products': products,
            'product_count': product_count,
        }
    return render(request, 'store/store.html',context)