from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path("", views.bestseller_products_list, name="home"),
    path("about_us/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("all_products/", views.products_list, name="products"),
    path("all_products_all/", views.products_list_all, name="products_all"),
    path("all_products/<int:ordering>", views.products_list, name="products"),
    path("all_products_all/<int:ordering>", views.products_list_all, name="products_all"),
    path("category/<int:category_id>/", views.products_list, name="products_by_category"),
    path("all/category/<int:category_id>/", views.products_list_all, name="products_all_by_category"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    path('product/new/', views.add_new_product, name='add_new_product'),
    path('category/new/', views.add_new_category, name='add_new_category'),
    path('manufacturer/new/', views.add_new_manufacturer, name='add_new_manufacturer'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('product/remove/<int:product_id>/', views.remove_product, name='remove_product'),
]
