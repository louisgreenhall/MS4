from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html')

def request(request):
    return render(request, 'home/requestform.html')

def signup(request):
    return render(request, 'home/signup.html')