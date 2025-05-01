from django.urls import path
from . import views

app_name = 'books'  # 👈 This is the namespace

urlpatterns = [
    path('show/', views.show, name='show'),
]
