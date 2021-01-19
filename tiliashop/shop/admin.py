from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Manufacturer
from .models import Category

admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Category)