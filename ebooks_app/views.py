from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import Book, Category, CustomUser, Review
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    books = Book.objects.filter(status='published')[:5]
    categories = Category.objects.all().order_by('?')[:8]
    
    return render(request, 'home.html', { 'books': books, 'categories': categories })

def books(request):
    books_per_page = 5
    page_number = request.GET.get('page', 1)
    all_books = Book.objects.filter(status='published')
    paginator = Paginator(all_books, books_per_page)
    paginated_books = paginator.get_page(page_number)

    return render(request, 'books.html', { 'books': paginated_books })

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'book_detail.html', { 'book': book, 'reviews': reviews })

def authors(request):
    authors_per_page = 10
    page_number = request.GET.get('page', 1)
    all_authors = CustomUser.objects.filter(user_type='author')
    paginator = Paginator(all_authors, authors_per_page)
    paginated_authors = paginator.get_page(page_number)

    return render(request, 'authors.html', { 'authors': paginated_authors })

def about(request):
    return render(request, 'about.html', { })

def cart(request):
    return render(request, 'cart.html', { })

def login(request):
    return render(request, 'login.html', { })

def register(request):
    return render(request, 'register.html', { })

def contact(request):
    return render(request, 'contact.html', { })

