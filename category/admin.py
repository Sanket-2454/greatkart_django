from django.contrib import admin
from .models import Category 
# Register your models here.

# This is for the auto slug as category_name


class CategoryAdmin(admin.ModelAdmin):
    # auto slug 
    prepopulated_fields = {'slug': ('category_name',)}
    # to display to admin 
    list_display = ("category_name", "slug")
    

admin.site.register(Category, CategoryAdmin)
