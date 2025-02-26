from django.db import models
from category.models import Category
from django.urls import reverse
from django.db.models.deletion import CASCADE
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField() 
    is_available = models.BooleanField(default=True)
    #Category is model here or what should happen to product when we delete a Category 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail',args=[self.category.slug, self.slug])#here self is product and category.slug is the categorymodel slug which is connected through forigen key 
    
    def __str__(self):
        return self.product_name

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category="color", is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category="size", is_active=True)

varition_category_choice=(
    ('color','color'),
    ('size','size'))

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # on_delete because the once the product is delted product variation is deleted and here we use prodcut because the we want the particular product
    variation_category = models.CharField(max_length=100, choices=varition_category_choice)  # this choices make a dropdown list in the admin panel 
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) # to check the vartion is active or not 
    created_date = models.DateTimeField(auto_now=True)
    
    objects = VariationManager() # tell the we make manager for your model 
    
    def __str__(self):
        return self.variation_value