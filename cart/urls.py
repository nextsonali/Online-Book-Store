from django.urls import path
from . import views

app_name = 'cart'  # 👈 This is the namespace

urlpatterns = [
    path('view_cart', views.view_cart, name='view_cart'),
    path('add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
