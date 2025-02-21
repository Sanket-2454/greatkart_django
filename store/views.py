from django.shortcuts import render, get_object_or_404
from . models import Product
from category.models import Category
# Create your views here.


def store(request, category_slug=None):
    
    categories = None 
    products = None 
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        # first decides the category and pass to the category 
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count() # here count is the python builtin method and we count the all product
        
    context = {
        'products': products,
        'product_count': product_count, # making available to the store.html
    }
    return render(request, 'store/store.html', context)

# category_slug,product_slug


def product_detail(request, category_slug, product_slug):
    try:
        # Fetch product using category slug and product slug
        single_product = Product.objects.get(category__slug= category_slug, slug=product_slug) # here we matching category__slug to the url
    except Exception as e:
        raise e 
        
    # Context dictionary to pass to the template
    context = {
        "single_product": single_product,
    }

    # Render the template with the context
    return render(request, 'store/product_detail.html', context)