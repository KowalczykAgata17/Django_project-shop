
from django import forms
from .models import Product, Category, Manufacturer


class AddProduct(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'manufacturer', 'name',
                  'image', 'description', 'price', 'stock',
                  'available', 'new', 'bestseller',)


class AddCategory(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description',)


class AddManufacturer(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = ('name', 'description', )
