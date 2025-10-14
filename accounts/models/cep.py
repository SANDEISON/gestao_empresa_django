from django.db import models
from accounts.models.logradouro import Logradouro
# -----------------------------
# Cep
# -----------------------------
class Cep(models.Model):
    codigo = models.CharField(max_length=9, unique=True)
    logradouro = models.ForeignKey(Logradouro, on_delete=models.CASCADE, related_name="ceps")

    def __str__(self):
        return f"{self.codigo} - {self.logradouro}"