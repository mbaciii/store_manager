# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.cashier_view, name='cashier_view'),
    path('register-sale/', views.register_sale, name='register_sale'),  # Add this line
]
