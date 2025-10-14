from django.db import models
from accounts.models.cidade import Cidade
from accounts.models.tipo_logradouro import TipoLogradouro
# -----------------------------
# Logradouro
# -----------------------------
class Logradouro(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name="logradouros")
    tipo = models.ForeignKey(TipoLogradouro, on_delete=models.PROTECT, related_name="logradouros")

    def __str__(self):
        return f"{self.tipo.nome} {self.nome}, {self.cidade.nome}"