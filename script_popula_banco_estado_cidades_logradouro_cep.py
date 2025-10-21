import os
import random
from faker import Faker

fake = Faker('pt_BR')  # gera nomes, endereços, CPFs, etc. em português
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.contrib.auth.models import User
from accounts.models.cep import Cep
from accounts.models.endereco import Endereco
from accounts.models.logradouro import Logradouro
from accounts.models.pessoa import Pessoa
from accounts.models.tipo_logradouro import TipoLogradouro
from accounts.models.cidade import Cidade
from accounts.models.estado import Estado
from accounts.models.pessoa_endereco import PessoaEndereco



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

tipos = ["Rua", "Avenida", "Travessa", "Alameda", "Condomínio" ,"Rodovia" , "Lote"]
for nome in tipos:
    TipoLogradouro.objects.get_or_create(nome=nome)
print("Tipos de logradouro populados.")


cidades = Cidade.objects.all()[:2000]  # apenas 2000 cidades para exemplo
tipos = list(TipoLogradouro.objects.all())

for cidade in cidades:
    for _ in range(50):
        tipo = random.choice(tipos)
        nome = f"{tipo.nome} {fake.last_name()}"
        logradouro, _ = Logradouro.objects.get_or_create(
            nome=nome,
            cidade=cidade,
            tipo=tipo
        )
print("Logradouros populados.")

ceps_gerados = set()
for logradouro in Logradouro.objects.all():
    codigo = fake.postcode()
    while codigo in ceps_gerados:
        codigo = fake.postcode()
    ceps_gerados.add(codigo)
    cep, _ = Cep.objects.get_or_create(codigo=codigo, logradouro=logradouro)

print("CEPs populados.")

enderecos = list(Endereco.objects.all())
ceps = list(Cep.objects.all())
cidades = list(Cidade.objects.all())
logradouros = list(Logradouro.objects.all())
estados = list(Estado.objects.all())

for i in range(1000):
    username = fake.user_name() + str(i) + '@gmail.com'
    user = User.objects.create_user(
        username=username,
        email=username,
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
    # Cria a pessoa sem informar endereço
    cpf_gerados = set()
    codigo = fake.cpf()
    while codigo in cpf_gerados:
        codigo = fake.cpf()
    pessoa = Pessoa.objects.create(
        user=user,
        cpf= codigo,
        rg= str(random.randint(1000000, 9999999)),
        telefone= fake.phone_number(),
        data_nascimento= fake.date_of_birth(minimum_age=18, maximum_age=65),
    )
    cpf_gerados.add(codigo)
    PessoaEndereco.objects.get_or_create(
        pessoa=pessoa,
        endereco=endereco,
    )

print("2000 pessoas criadas com sucesso!")