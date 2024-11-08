from django.urls import path, re_path, include, register_converter
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.books, name='books'),
    path('books/<int:book_id>', views.book_detail, name='book_detail'),
    path('authors', views.authors, name='authors'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'), 
]
