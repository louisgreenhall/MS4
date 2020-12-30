from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import serializers, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from home.models import Request

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html', {'user':'test'})

def request(request):
    if request.method == 'POST':
        req = Request()
        req.title =  request.POST.get('title')
        req.description =  request.POST.get('description')
        req.draw_type = request.POST.get('draw_type')
        req.colour = request.POST.get('colour')
        req.backing = request.POST.get('backing')
        req.files = request.POST.get('files')
        req.author = request.user
        req.status = 'Awaiting Deposit'
        req.save()
        return redirect(req)
    else:
        return render(request, 'home/requestform.html')

def requests_mine(request):
    requests = Request.objects.filter(author=request.user)
    return render(request, 'home/requests.html', {'requests': requests})

def signup(request):
    if request.method == 'POST':
        print(request)
        try:

            # Get data from request
            username = request.POST.get('username')
            
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
            email = request.POST.get('email')
            confirm_email = request.POST.get('confirm_email')

            errors = {}

            # Check if passwords matched
            if password != confirm_password:
                errors['password_error'] = 'Passwords must match!'

            # Check if emails matched
            if email != confirm_email:
                errors['email_error'] = 'Email addresses must match!'

            # Check if there were any errors
            if len(errors.keys()) > 0:
                return render(request, 'home/signup.html', {
                    'errors': errors,
                    'username': username, 
                    'email': email, 
                    'confirm_email': confirm_email,
                    'success': False

                })
            
            # Create the user, everything is good
            user = User.objects.create_user(username, email, password)

            user.save()

            return render(request, 'home/signup.html', {
                'errors': {},
                'username': '', 
                'email': '', 
                'confirm_email': '',
                'success': True,
                'message': 'User successfully created'

            })
        
        # The user with this username already exists, return an error
        except IntegrityError: 
            return render(request, 'home/signup.html', {
                'errors': {},
                'username': username, 
                'email': email, 
                'confirm_email': confirm_email,
                'success': False,
                'message': 'A user with this already exists'
            })

        # Required fields were missing from the request, return an error
        return render(request, 'home/signup.html', {
            'errors': {},
            'username': '', 
            'email': '', 
            'confirm_email': '',
            'success': False,
            'message': ''
        })

    else: 
        return render(request, 'home/signup.html', {
            'errors': {},
            'username': '', 
            'email': '', 
            'confirm_email': '',
            'success': False,
            'message': ''
        })
