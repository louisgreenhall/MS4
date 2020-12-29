from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import serializers, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html', {'user':'test'})

def request(request):
    return render(request, 'home/requestform.html')

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

@api_view(['POST'])
def post_login(request):
    try: 
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            # The user exists and has authenticated properly
            u = User.objects.get(username='lgree')
            print(u.is_superuser)
            return JsonResponse({'success': True},safe=False)
        else:
            # Username or password provided was incorrect, return an unauthorised error
            return JsonResponse({'success': False}, status=status.HTTP_401_UNAUTHORIZED) 
    # Something else went wrong, return an unauthorised error
    except: 
        return JsonResponse({'success': False}, status=status.HTTP_401_UNAUTHORIZED) 


