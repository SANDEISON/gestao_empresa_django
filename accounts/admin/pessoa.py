from django.contrib import admin
from accounts.models.pessoa import Pessoa
from accounts.models.pessoa_endereco import PessoaEndereco


# Inline para histórico de endereços
class PessoaEnderecoInline(admin.TabularInline):  # ou StackedInline se preferir
    model = PessoaEndereco
    extra = 0
    autocomplete_fields = ['endereco']  # permite pesquisar o endereço em vez de dropdown longo
    fields = ('endereco', 'data_inicio', 'data_fim', 'ativo')
    readonly_fields = ('data_inicio',)  # data de início preenchida automaticamente


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'telefone', 'data_nascimento', 'endereco_atual')
    search_fields = ('cpf', 'user__username', 'user__first_name', 'user__last_name')
    list_filter = ('data_nascimento',)
    inlines = [PessoaEnderecoInline]  # adiciona o inline