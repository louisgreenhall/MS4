from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('requests/<int:request_id>/checkout/deposit', views.checkout_deposit, name='checkout_deposit'),
    path('requests/<int:request_id>/checkout/final', views.checkout_final, name='checkout_final'),
    # path('payment', views.payment, name='payment')
    
]
