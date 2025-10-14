from django.db import models
# -----------------------------
# Estado
# -----------------------------
class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"