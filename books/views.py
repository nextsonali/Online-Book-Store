from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from cart.models import CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def show(request):
    books = Book.objects.all()
    cart_books = []
    if request.user.is_authenticated:
        cart_books = CartItem.objects.filter(user=request.user).values_list('book', flat=True)
    return render(request, 'books/book_list.html', {'books': books, 'cart_books': cart_books})

@login_required(login_url='users:login')  # 👈 Redirects to login if not authenticated
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, f"Quantity updated for '{book.title}'.")
    else:
        messages.success(request, f"'{book.title}' added to cart.")

    return redirect('books:show')

@login_required(login_url='users:login')  # 👈 Redirects to login if not authenticated
def remove_from_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    try:
        cart_item = CartItem.objects.get(user=request.user, book=book)
        cart_item.delete()
        messages.warning(request, f"'{book.title}' removed from cart.")
    except CartItem.DoesNotExist:
        messages.error(request, "This book is not in your cart.")

    return redirect('books:show')