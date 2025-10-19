from django.db import models
# -----------------------------
# Tipo Logradouro
# -----------------------------
class TipoLogradouro(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tipo de Logradouro" # Nome legível no singular (mostrado no admin)
        verbose_name_plural = "Tipos de Logradouro" # Nome legível no plural
        ordering = ['nome'] # Define a ordem padrão ao listar objetos (ex.: ['nome'])
        db_table = 'tipo_logradouro' # Define o nome da tabela no banco


    def __str__(self):
        return self.nome