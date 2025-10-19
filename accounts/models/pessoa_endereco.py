from django.db import models
from accounts.models.endereco import Endereco
from accounts.models.pessoa import Pessoa
# -----------------------------
#  Endereco da Pessoa
# -----------------------------

class PessoaEndereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, )
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Histórico de Endereço" # Nome legível no singular (mostrado no admin)
        verbose_name_plural = "Históricos de Endereço" # Nome legível no plural
        ordering = ['-data_inicio'] # Define a ordem padrão ao listar objetos (ex.: ['nome'])
        db_table = 'pessoa_endereco' # Define o nome da tabela no banco
        unique_together = ('pessoa', 'endereco') # Garante unicidade combinada de campos (ex.: pessoa + endereco)

    def __str__(self):
        status = "Ativo" if self.ativo else "Inativo"
        return f"{self.pessoa} - {self.endereco} ({status})"