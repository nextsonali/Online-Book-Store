from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book
from .models import CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

@login_required(login_url='users:login')
def view_cart(request):
    items = CartItem.objects.filter(user=request.user)
    response_data = []
    total = 0
    for item in items:
        item_total = item.quantity * item.book.price
        print(item_total)
        total += item_total
        response_data.append({
            "book_id": item.book.id,
            "book_title": item.book.title,
            "book_author": item.book.author,
            "book_price": item.book.price,
            "quantity": item.quantity,
            "total_price": item_total
        })
    #total = sum(item.total_price() for item in items)
    return render(request, 'cart/view_cart.html', {'items': response_data, 'total': total})

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
