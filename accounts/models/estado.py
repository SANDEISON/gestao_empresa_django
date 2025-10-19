from django.db import models
# -----------------------------
# Estado
# -----------------------------
class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2, unique=True)

    class Meta:
        verbose_name = "Estado" # Nome legível no singular (mostrado no admin)
        verbose_name_plural = "Estados" # Nome legível no plural
        ordering = ['nome'] # Define a ordem padrão ao listar objetos (ex.: ['nome'])
        db_table = 'estado' # Define o nome da tabela no banco

    def __str__(self):
        return f"{self.nome} ({self.sigla})"