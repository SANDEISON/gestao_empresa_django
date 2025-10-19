from django.db import models
from accounts.models.cep import Cep
from accounts.models.cidade import Cidade
from accounts.models.estado import Estado
from accounts.models.logradouro import Logradouro
# -----------------------------
# Endereco
# -----------------------------
class Endereco(models.Model):
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    logradouro = models.ForeignKey(Logradouro, on_delete=models.PROTECT)
    cep = models.ForeignKey(Cep, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Endereço" # Nome legível no singular (mostrado no admin)
        verbose_name_plural = "Endereços" # Nome legível no plural
        ordering = ['cidade', 'logradouro', 'numero'] # Define a ordem padrão ao listar objetos (ex.: ['cidade'])
        db_table = 'endereco' # Define o nome da tabela no banco


    def __str__(self):
        return f"{self.logradouro} nº {self.numero}"

