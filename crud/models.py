from django.db import models
from django.db.models.base import Model
from django.utils.translation import gettext_lazy as _
from suppliers.models import Fornecedor

# Create your models here.
# class Entidade(models.Model):
#     entidade_nome = models.CharField(max_length=200)
#     #True - Supervisor / False - Vendedor
#     entidade_status = models.BooleanField(default=False)


class Estoque(models.Model):
    estoque_produto_total = models.IntegerField(default=1)
    estoque_entrada_produto = models.IntegerField(default=1)
    estoque_saida_produto = models.IntegerField(default=1)


class Produto(models.Model):
    class ProdutoTipos(models.TextChoices):
        BEVERAGES = 'BE', _('coffee/tea, juice, soda')
        BREAD_BAKERY = 'BR', _('sandwich loaves, dinner rolls, tortillas, bagels')
        CANNED_JARRED = 'CA', _('vegetables, spaghetti sauce, ketchup')
        DAIRY = 'DA', _('cheeses, eggs, milk, yogurt, butter')
        DRY_BAKING = 'DR', _('cereals, flour, sugar, pasta, mixes')
        FROZEN_FOODS = 'FR', _('waffles, vegetables, individual meals, ice cream')
        MEAT = 'ME', _('lunch meat, poultry, beef, pork')
        PRODUCE = 'PR', _('fruits, vegetables')
        CLEANERS = 'CL', _('all - purpose, laundry detergent, dishwashing liquid/detergent')
        PAPER_GOODS = 'PA', _('paper towels, toilet paper, aluminum foil, sandwich bags')
        PERSONAL_CARE = 'PE', _('shampoo, soap, hand soap, shaving cream')
        OTHER = 'OT', _('baby items, pet items, batteries, greeting cards')

    produto_nome = models.CharField(max_length=200, default='Produto')
    produto_tipo = models.CharField(max_length=2, choices=ProdutoTipos.choices, default=ProdutoTipos.OTHER)
    produto_preco = models.FloatField(default=0.0)
    produto_quantidade = models.IntegerField(default=1)
    produto_nome_vendedor = models.CharField(max_length=200, default='Vendedor')
    produto_venda_data = models.DateField(auto_now_add=True)
    fornecedor_pk = models.ManyToManyField(Fornecedor)


