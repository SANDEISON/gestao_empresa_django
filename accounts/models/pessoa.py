from django.db import models
from django.contrib.auth.models import User
from accounts.models.endereco import Endereco
# -----------------------------
# PESSOA
# -----------------------------
class Pessoa(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Usuário', on_delete=models.CASCADE)  # deletar pessoa e usuário juntos
    cpf = models.CharField(max_length=14, verbose_name=u'CPF',unique=True)
    rg = models.CharField(max_length=30, verbose_name=u'RG', null=True, blank=True)
    telefone = models.CharField(max_length=20, verbose_name=u'Telefone',blank=True, null=True)
    data_nascimento = models.DateField(verbose_name=u'Data de nascimento')
    enderecos = models.ManyToManyField(Endereco,through='PessoaEndereco', related_name='pessoas')

    class Meta:
        verbose_name = "Pessoa" # Nome legível no singular (mostrado no admin)
        verbose_name_plural = "Pessoas" # Nome legível no plural
        ordering = ['user__first_name'] # Define a ordem padrão ao listar objetos (ex.: ['nome'])
        db_table = 'pessoa' # Define o nome da tabela no banco

    def __str__(self):
        return self.user.username

    # O @property é um decorador do Python que transforma um metodo de uma classe em um atributo somente de leitura.
    # Ou seja:
    # Você escreve e define o metodo como se fosse uma função, mas o acessa como se fosse um atributo — sem precisar dos parênteses ().
    @property
    def endereco_atual(self):
        """Retorna o endereço ativo (atual) da pessoa"""
        endereco_rel = self.pessoaenderecos.filter(ativo=True).first()
        return endereco_rel.endereco if endereco_rel else None