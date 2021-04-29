from django.db import models
from products.models import Produto

# Create your models here.

class Estoque(models.Model):
    estoque_total_produtos = models.IntegerField(default=0)
    estoque_total_ativo_produtos = models.IntegerField(default=0)
    estoque_produtos_entrada = models.IntegerField(default=0)
    estoque_produtos_saida = models.IntegerField(default=0)

    produto_pk = models.ManyToManyField(Produto)
