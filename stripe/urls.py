from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    
]
