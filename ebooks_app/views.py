from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from .models import Book, Category, CustomUser, Review, Cart, CartItem, Enquiry
from django.core.paginator import Paginator
from decimal import Decimal
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from .forms import EnquiryForm, RegisterForm
from django.contrib import messages

# Create your views here.

def home(request):
    books = Book.objects.filter(status='published')[:5]
    categories = Category.objects.all().order_by('?')[:8]

    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enquiry submitted successfully')
            return redirect('home')
    else:
        if request.user.is_authenticated:
            form = EnquiryForm(initial={ 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email': request.user.email, 'phone': request.user.phone })
        else:
            form = EnquiryForm()
    
    return render(request, 'home.html', { 'books': books, 'categories': categories, 'form': form })

def books(request):
    books_per_page = 10
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

def author_detail(request, author_id):
    author = CustomUser.objects.get(id=author_id)
    books = Book.objects.filter(author=author)
    return render(request, 'author_detail.html', { 'author': author, 'books': books })

def about(request):
    return render(request, 'about.html', { })

def cart(request):
    if request.user.is_authenticated:   
        cart = Cart.objects.filter(user=request.user).first()
        cart_items = CartItem.objects.filter(cart=cart).order_by('-id')

        total_price = Decimal(0)   
        tax = Decimal(0)
        grand_total = Decimal(0)

        for cart_item in cart_items:
            total_price += cart_item.book.price * cart_item.quantity
        
        tax = round(float(total_price) * .10, 2)
        grand_total = round(float(total_price) + float(tax), 2)
    else:
        return redirect('login')

    return render(request, 'cart.html', { 'cart_items': cart_items, 'total_price': total_price, 'tax': tax, 'grand_total': grand_total })

def remove_from_cart(request, cart_item_id):
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()
    else:
        return redirect('login')
    return redirect('cart')

def update_cart_item(request, cart_item_id):
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.quantity = request.POST.get('quantity')
        cart_item.save()
    else:
        return redirect('login')
    return redirect('cart')

def add_to_cart(request, book_id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=book_id)
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_item = CartItem.objects.filter(cart=cart, book=book).first()
            if cart_item:
                cart_item.quantity += 1
                cart_item.save()
            else:
                cart_item = CartItem.objects.create(cart=cart, book=book, quantity=1)
                cart_item.save()
        else:
            cart = Cart.objects.create(user=request.user)
            cart_item = CartItem.objects.create(cart=cart, book=book, quantity=1)
            cart_item.save()
    else:
        return redirect('login')
    return redirect('cart')

def checkout(request):
    return render(request, 'checkout.html', { })

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html', { })

def register(request):
    if request.user.is_authenticated:
        return redirect('home')


    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', { 'form': form })

def logout(request):
    auth_logout(request)
    return redirect('home')

def contact(request):
    return render(request, 'contact.html', { })

