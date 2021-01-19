from django.shortcuts import render
from .models import OrderItem, Order
from .forms import CreateOrderForm
from cart.cart import Cart


def create_order(request):
    cart = Cart(request) #uzyskujemy aktualny koszyk z sesji
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request, 'orders/created_order.html', {'order': order})
    else:
        form = CreateOrderForm()
    return render(request, 'orders/create_order.html', {'cart': cart, 'form': form})


def orders_list(request):
    orders = Order.objects.all()

    context = {
        'orders': orders
    }
    return render(request, 'orders/list.html', context)

