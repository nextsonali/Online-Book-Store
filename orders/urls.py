from django.urls import path
from . import views
app_name = 'orders'  # 👈 This is the namespace

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('history/', views.order_history, name='order_history'),
]
