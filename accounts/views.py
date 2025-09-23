from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        pass
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        #
        # user = authenticate(request, username=username, password=password)
        #
        # if user is not None:
        #     login(request, user)
        #     messages.success(request, f'Bem-vindo, {user.username}!')
        #     return redirect('home')
        # else:
        #     messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'accounts/login.html')
