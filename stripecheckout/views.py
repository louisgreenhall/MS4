from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import serializers, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from home.models import Request, Comment

import stripe
stripe.api_key = "sk_test_51I4TYWGBayL5RWdKUUBs1ud8l0WcK2bGcK7vBth8KqUqgpTJDp5WRNIxHlsvoM6a2KvvO1Cc9EL1HIj4iFby4RuX00WWXTNQIK"

# Create your views here.

def checkout_deposit(request, request_id):
    req = Request.objects.get(id=request_id)

    return render(request, 'stripe/checkout.html', {'title': req.title, 'total': 30.00, 'line_items': [{'name': 'Deposit', 'amount': 30.00}]})



def checkout_final(request, request_id):
    req = Request.objects.get(id=request_id)

    return render(request, 'stripe/checkout.html')

def success(request):
    session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(session_id)
    print(session)
    if session['amount_total']/100 == 30:
        return render(request, 'stripe/success.html', {'payment_status': session['payment_status'], 'amount': session['amount_total']/100, 'continue_url': session['client_reference_id'].replace("/deposit", "/deposit_paid")})
        
    return render(request, 'stripe/success.html', {'payment_status': session['payment_status'], 'amount': session['amount_total']/100})

def deposit_paid(request, request_id):
    req = Request.objects.get(id=request_id)
    req.status = "Deposit Received"
    req.save()
    return redirect(req)