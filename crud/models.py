from django.db import models
from django.db.models.base import Model
from datetime import date

# Create your models here.
# class Entidade(models.Model):
#     entidade_nome = models.CharField(max_length=200)
#     #True - Supervisor / False - Vendedor
#     entidade_status = models.BooleanField(default=False)


class Estoque(models.Model):
    estoque_produto_total = models.IntegerField(default=1)
    estoque_entrada_produto = models.IntegerField(default=10)
    estoque_saida_produto = models.IntegerField(default=10)
    produto_pk = models.ForeignKey('Produto', on_delete=models.CASCADE)


class Produto(models.Model):
    produto_nome = models.CharField(max_length=200, default='meu nome')

    produto_quantidade = models.IntegerField(default=1)
    produto_nome_vendedor = models.CharField(max_length=200, default='Juriscleyton')
    produto_venda_data = models.DateField(default=date.today())
    fornecedor_pk = models.ManyToManyField('Fornecedor')


class Fornecedor(models.Model):
    fornecedor_nome = models.CharField(max_length=200, default='Toninho')
