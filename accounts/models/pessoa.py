from django.db import models
from django.contrib.auth.models import User
from accounts.models.endereco import Endereco
# -----------------------------
# PESSOA
# -----------------------------
class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username