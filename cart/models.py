# cart/models.py
from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book

User = get_user_model()

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.book.title} for {self.user.username}"

    def total_price(self):
        return self.quantity * self.book.price
