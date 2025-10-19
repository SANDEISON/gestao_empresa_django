from django.db import models
from accounts.models.estado import Estado
# -----------------------------
# Cidade
# -----------------------------
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cidade" # Nome legível no singular (mostrado no admin)
        verbose_name_plural = "Cidades" # Nome legível no plural
        ordering = ['nome'] # Define a ordem padrão ao listar objetos (ex.: ['nome'])
        db_table = 'cidade' # Define o nome da tabela no banco
        unique_together = ('nome', 'estado')  # Garante unicidade combinada de campos (ex.: cidade + estado)

    def __str__(self):
        return f"{self.nome} - {self.estado.sigla}"
