from django.db import models
from accounts.models.cidade import Cidade
from accounts.models.tipo_logradouro import TipoLogradouro
# -----------------------------
# Logradouro
# -----------------------------
class Logradouro(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoLogradouro, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Logradouro" # Nome legível no singular (mostrado no admin)
        verbose_name_plural = "Logradouros" # Nome legível no plural
        ordering = ['nome'] # Define a ordem padrão ao listar objetos (ex.: ['nome'])
        db_table = 'logradouro' # Define o nome da tabela no banco
        unique_together = ('nome', 'cidade', 'tipo') # Garante unicidade combinada de campos (ex.: cidade + estado)

    def __str__(self):
        return f"{self.tipo.nome} {self.nome}, {self.cidade.nome}"
