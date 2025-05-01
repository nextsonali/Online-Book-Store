from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from cart.models import CartItem
from django.contrib import messages

def show(request): 
    books = Book.objects.all()
    cart_books = []

    if request.user.is_authenticated:
        cart_books = CartItem.objects.filter(user=request.user).values_list('book_id', flat=True)

    return render(request, 'books/book_list.html', {
        'books': books,
        'cart_books': cart_books
    })

