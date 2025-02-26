from django.contrib import admin
from .models import Product
from .models import Variation
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "price", "stock", "category", "modified_date", "is_available")
    # prepopulate slug
    prepopulated_fields = {'slug':('product_name',)} # make sure this is the tuple
    
    
    
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active')
    list_editable = ('is_active',) # make a checkbox for the is_active admin
    list_filter = ('product','variation_category','variation_value') # add the filter on the left side on the admin 

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)