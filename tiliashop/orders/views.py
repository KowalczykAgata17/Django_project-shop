#import weasyprint
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from .models import OrderItem, Order
from .forms import CreateOrderForm, EditOrderForm
from cart.cart import Cart



def create_order(request):
    cart = Cart(request) #uzyskujemy aktualny koszyk z sesji
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            cart.clear()
            messages.info(request, 'Zamówienie zostało złożone')
            return render(request, 'orders/created_order.html', {'order': order})
    else:
        form = CreateOrderForm()
    return render(request, 'orders/create_order.html', {'cart': cart, 'form': form})


@login_required(login_url='/login')
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {
        'order': order
    }
    return render(request, 'orders/detail.html', context)


@login_required(login_url='/login')
def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = EditOrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            messages.info(request, 'Zamówienie zostało zmienione')
            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = EditOrderForm(instance=order)
    return render(request, 'orders/edit_order.html', {'form': form, 'order': order})


@login_required(login_url='/login')
def orders_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'orders/list.html', context)