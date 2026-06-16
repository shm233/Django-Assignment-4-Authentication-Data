from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from auth_app.models import *

# Create your views here.

def sign_up(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            CustomUser.objects.create_user(
                username = username,
                email = email,
                address = address,
                password = password
            )
            return redirect('sign_in')
    return render(request, 'sign-up.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_id = authenticate(username=username, password=password)
        if user_id:
            login(request, user_id)
            return redirect('home_page')
    return render(request, 'sign-in.html')

@login_required
def sign_out(request):
    logout(request)
    return redirect('sign_in')

def home_page(request):
    return render(request, 'dashboard.html')
