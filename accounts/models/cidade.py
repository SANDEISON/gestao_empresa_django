from django.db import models
from accounts.models.estado import Estado
# -----------------------------
# Cidade
# -----------------------------
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="cidades")

    def __str__(self):
        return f"{self.nome} - {self.estado.sigla}"