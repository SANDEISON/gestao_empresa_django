import random

import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from accounts.models.cep import Cep
from accounts.models.cidade import Cidade
from accounts.models.endereco import Endereco
from accounts.models.estado import Estado
from accounts.models.logradouro import Logradouro
from accounts.models.pessoa import Pessoa
from accounts.models.tipo_logradouro import TipoLogradouro
from accounts.scripts.popular_banco import fake


# Create your views here.

def index(request):
    print("Buscando estados e cidades do IBGE...")
    estados_response = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados").json()
    for estado_data in estados_response:
        estado, created = Estado.objects.get_or_create(
            nome=estado_data['nome'],
            sigla=estado_data['sigla']
        )

        cidades_response = requests.get(
            f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado_data['id']}/municipios"
        ).json()

        for cidade_data in cidades_response:
            Cidade.objects.get_or_create(
                nome=cidade_data['nome'],
                estado=estado
            )

    print("Estados e cidades populados com sucesso!")


    tipos = ["Rua", "Avenida", "Travessa", "Alameda", "Rodovia"]
    for nome in tipos:
        TipoLogradouro.objects.get_or_create(nome=nome)
    print("Tipos de logradouro populados.")

    cidades = Cidade.objects.all()[:5]  # apenas 5 cidades para exemplo
    tipos = list(TipoLogradouro.objects.all())

    for cidade in cidades:
        for _ in range(10):
            tipo = random.choice(tipos)
            nome = f"{tipo.nome} {fake.last_name()}"
            logradouro, _ = Logradouro.objects.get_or_create(
                nome=nome,
                cidade=cidade,
                tipo=tipo
            )
            Cep.objects.get_or_create(
                codigo=fake.postcode().replace('-', ''),
                logradouro=logradouro
            )
    print("Logradouros e CEPs populados.")

    enderecos = list(Endereco.objects.all())
    ceps = list(Cep.objects.all())
    cidades = list(Cidade.objects.all())
    logradouros = list(Logradouro.objects.all())
    estados = list(Estado.objects.all())

    for i in range(500):
        username = fake.user_name() + str(i) + '@gmail.com'
        user = User.objects.create_user(
            username=username,
            email=fake.email(),
            password="123456789"
        )
        endereco = Endereco.objects.create(
            numero=str(fake.building_number()),
            complemento='',
            estado=random.choice(estados),
            cidade=random.choice(cidades),
            logradouro=random.choice(logradouros),
            cep=random.choice(ceps),
        )
        Pessoa.objects.create(
            user=user,
            endereco=endereco
        )
    print("500 pessoas criadas com sucesso!")

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