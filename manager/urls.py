# urls.py
from django.urls import path
from . import views

from .views import custom_login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('manager/', views.manager, name='manager'),

    path('accounts/login/', custom_login, name='custom_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
