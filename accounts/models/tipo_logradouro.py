from django.db import models
# -----------------------------
# Tipo Logradouro
# -----------------------------
class TipoLogradouro(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome