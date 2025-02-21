from django.contrib import admin
from .models import Product 
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "price", "stock", "category", "modified_date", "is_available")
    # prepopulate slug
    prepopulated_fields = {'slug':('product_name',)} # make sure this is the tuple
admin.site.register(Product, ProductAdmin)