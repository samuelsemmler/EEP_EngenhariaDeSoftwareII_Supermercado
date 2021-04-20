from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    fornecedor_nome = models.CharField(max_length=200, default='Fornecedor')
    fornecedor_nome_empresa = models.CharField(max_length=200, default='Company')
    fornecedor_email = models.EmailField(max_length=254, blank=True)
    fornecedor_endereco = models.CharField(max_length=200, default='Localization')
    fornecedor_cidade = models.CharField(max_length=200, default='Localization')
    fornecedor_pais = models.CharField(max_length=200, default='Localization')
    fornecedor_comentarios = models.TextField(blank=True)