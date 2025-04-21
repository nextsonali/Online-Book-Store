from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book
from .models import CartItem

def view_cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in items)
    return render(request, 'cart/view_cart.html', {'items': items, 'total': total})

def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    if not created:
        item.quantity += 1
    item.save()
    return redirect('view_cart')

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('view_cart')
