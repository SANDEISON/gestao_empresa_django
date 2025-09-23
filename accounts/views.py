from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.

def index(request):

    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('email')
        password = request.POST.get('senha')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}!')
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'accounts/login.html')
