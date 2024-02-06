from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import FormLogin
# Create your views here.

def login_view(request):
    form = FormLogin()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login/dashboard')
        
    return render(request, 'login/login_view.html', {'form':form})

def dashboard(request):
    context = {}
    return render(request, 'login/dashboard.html', context)