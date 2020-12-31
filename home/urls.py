from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', views.index, name='home'),
    path('request', views.request, name='request'),
    path('signup', views.signup, name='signup'),
    path('login', LoginView.as_view(template_name='home/login.html'), name='login', ),
    path('logout', LogoutView.as_view(template_name='home/logged_out.html'), name='logout'),
    path('requests/mine', views.requests_mine, name='requests_mine'),
    path('requests/all', views.requests_all, name='requests_all'),

    path('requests/<int:request_id>/', views.request_individual, name='request_individual'),
    path('requests/<int:request_id>/add_comment', views.request_individual, name="submit_comment")
]
