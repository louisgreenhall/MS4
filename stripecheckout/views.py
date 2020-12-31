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

    return render(request, 'stripe/checkout.html', {'type': 'deposit', 'title': req.title, 'total': 30.00, 'line_items': [{'name': 'Deposit', 'amount': 30.00}]})



def checkout_final(request, request_id):
    req = Request.objects.get(id=request_id)
    totalCost = 0
    line_items = []

    if req.draw_type == 'hand_drawn':
        totalCost += 15
        line_items.append({'name': 'hand_drawn', 'amount': 15.00})

    if req.draw_type == 'digital':
        totalCost += 10
        line_items.append({'name':'digital', 'amount': 10.00})


    if req.backing == 'canvas':
        totalCost += 5
        line_items.append({'name': 'canvas', 'amount': 5.00})


    if req.backing == 'framed':
        totalCost += 3
        line_items.append({'name': 'framed', 'amount': 3.00})


    if req.files == 'included':
        totalCost += 5
        line_items.append({'name': 'included', 'amount': 5.00})


    if req.files == 'sketches':
        totalCost += 5
        line_items.append({'name': 'sketches', 'amount': 5.00})


    
    return render(request, 'stripe/checkout.html', {'type': 'final','title': req.title, 'total': totalCost, 'line_items': line_items})

def success(request):
    session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(session_id)
    print(session)
    if session['amount_total']/100 == 30:
        return render(request, 'stripe/success.html', {'payment_status': session['payment_status'], 'amount': session['amount_total']/100, 'continue_url': session['client_reference_id'].replace("/deposit", "/deposit_paid")})
    
    else:
        return render(request, 'stripe/success.html', {'payment_status': session['payment_status'], 'amount': session['amount_total']/100, 'continue_url': session['client_reference_id'].replace("/final", "/final_paid")})

def deposit_paid(request, request_id):
    req = Request.objects.get(id=request_id)
    req.status = "Deposit Received"
    req.save()
    return redirect(req)

def final_paid(request, request_id):
    req = Request.objects.get(id=request_id)
    req.status = "Payment Received"
    req.save()
    return redirect(req)