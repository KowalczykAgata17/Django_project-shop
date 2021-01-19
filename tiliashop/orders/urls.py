from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('orders_list/', views.orders_list, name='orders_list'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/edit/<int:order_id>/', views.edit_order, name='edit_order'),
]
