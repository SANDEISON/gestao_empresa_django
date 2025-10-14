from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
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
            if user.is_superuser:
                return redirect('gerencia')
            else:
                return redirect('home')
            # premisao_grupos = user.get_group_permissions()
            # print(premisao_grupos)

        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def home_view(request):
    return render(request, 'home.html')


def gerencia_view(request):
    return render(request, 'gerencia.html')