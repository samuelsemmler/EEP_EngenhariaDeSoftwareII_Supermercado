from django.db import models
from django.utils.translation import gettext_lazy as _
from suppliers.models import Fornecedor

# Create your models here.
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
    produto_data_criacao = models.DateField(auto_now_add=True)
    fornecedor_pk = models.ManyToManyField(Fornecedor)