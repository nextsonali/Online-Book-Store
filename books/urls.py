from django.urls import path
from . import views

app_name = 'books'  # 👈 This is the namespace

urlpatterns = [
    path('show/', views.show, name='show'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:book_id>/', views.remove_from_cart, name='remove_from_cart'),
]
