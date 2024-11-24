from django.urls import path, re_path, include, register_converter
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.books, name='books'),
    path('books/<int:book_id>', views.book_detail, name='book_detail'),
    path('cart/remove/<int:cart_item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:cart_item_id>', views.update_cart_item, name='update_cart_item'),
    path('cart/add/<int:book_id>', views.add_to_cart, name='add_to_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('authors', views.authors, name='authors'),
    path('authors/<int:author_id>', views.author_detail, name='author_detail'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('orders', views.orders, name='orders'),
    path('order_success/<int:order_id>', views.order_success, name='order_success'),
    path('add_address', views.add_address, name='add_address'),
    path('edit_address/<int:address_id>', views.edit_address, name='edit_address'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'), 
    path('logout', views.logout, name='logout'),
]
