from django.contrib import admin
from accounts.views import RegisterView
from django.urls import path

urlpatterns = [
    # Register
    path('register/', RegisterView.as_view(), name='register')
]