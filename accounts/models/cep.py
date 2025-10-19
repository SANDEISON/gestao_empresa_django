from django.db import models
from accounts.models.logradouro import Logradouro
# -----------------------------
# Cep
# -----------------------------
class Cep(models.Model):
    codigo = models.CharField(max_length=9, unique=True)
    logradouro = models.ForeignKey(Logradouro, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "CEP" # Nome legível no singular (mostrado no admin)
        verbose_name_plural = "CEPs" # Nome legível no plural
        ordering = ['codigo'] # Define a ordem padrão ao listar objetos (ex.: ['nome'])
        db_table = 'cep' # Define o nome da tabela no banco


    def __str__(self):
        return f"{self.codigo} - {self.logradouro}"
