from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import AddProduct, AddCategory, AddManufacturer
from .models import Category, Product
from cart.forms import CartAddProductForm


def products_list(request, category_id=None, ordering=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)
    if ordering:
        if ordering == 1:
            products = products.order_by('name')
        elif ordering == 2:
            products = products.order_by('-name')
        elif ordering == 3:
            products = products.order_by('price')
        else:
            products = products.order_by('-price')

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/Products/list.html', context)


def bestseller_products_list(request):
    products = Product.objects.filter(available=True, bestseller=True)

    context = {
        'products': products
    }
    return render(request, 'shop/Products/home.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/Products/detail.html', context)


def home(request):
    return render(request, "shop/base.html", {})


@login_required(login_url='/login')
def products_list_all(request, category_id=None, ordering=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)
    if ordering:
        if ordering == 1:
            products = products.order_by('name')
        elif ordering == 2:
            products = products.order_by('-name')
        elif ordering == 3:
            products = products.order_by('price')
        else:
            products = products.order_by('-price')

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/Products/list.html', context)


@login_required(login_url='/login')
def add_new_product(request):
    if request.method == "POST":
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = AddProduct()
    return render(request, 'shop/Products/add_product.html', {'form': form})


@login_required(login_url='/login')
def add_new_category(request):
    if request.method == "POST":
        form = AddCategory(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('products_by_category', category_id=category.id)
    else:
        form = AddCategory()
    return render(request, 'shop/Products/add_category.html', {'form': form})


@login_required(login_url='/login')
def add_new_manufacturer(request):
    if request.method == "POST":
        form = AddManufacturer(request.POST, request.FILES)
        if form.is_valid():
            manufacturer = form.save(commit=False)
            manufacturer.save()
            return redirect('products')
    else:
        form = AddManufacturer()
    return render(request, 'shop/Products/add_manufacturer.html', {'form': form})


@login_required(login_url='/login')
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = AddProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            messages.info(request, 'Product has been changed')
            return redirect('product_detail', product_id=product.id)
    else:
        form = AddProduct(instance=product)
    return render(request, 'shop/Products/edit_product.html', {'form': form})


@login_required(login_url='/login')
def remove_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.info(request, 'Product has been removed')
    return redirect('products')

