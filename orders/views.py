from django.shortcuts import render, redirect
from cart.models import CartItem
from .models import Order, OrderItem

def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('view_cart')

    order = Order.objects.create(user=request.user)

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            book=item.book,
            quantity=item.quantity,
            price=item.book.price
        )
        item.delete()

    return redirect('orders:order_history')

def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_histroy.html', {'orders': orders})
