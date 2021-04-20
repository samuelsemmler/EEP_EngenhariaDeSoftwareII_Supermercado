# Generated by Django 3.2 on 2021-04-20 02:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoque',
            name='produto_pk',
        ),
        migrations.AddField(
            model_name='produto',
            name='produto_preco',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='produto',
            name='produto_tipo',
            field=models.CharField(choices=[('BE', 'coffee/tea, juice, soda'), ('BR', 'sandwich loaves, dinner rolls, tortillas, bagels'), ('CA', 'vegetables, spaghetti sauce, ketchup'), ('DA', 'cheeses, eggs, milk, yogurt, butter'), ('DR', 'cereals, flour, sugar, pasta, mixes'), ('FR', 'waffles, vegetables, individual meals, ice cream'), ('ME', 'lunch meat, poultry, beef, pork'), ('PR', 'fruits, vegetables'), ('CL', 'all - purpose, laundry detergent, dishwashing liquid/detergent'), ('PA', 'paper towels, toilet paper, aluminum foil, sandwich bags'), ('PE', 'shampoo, soap, hand soap, shaving cream'), ('OT', 'baby items, pet items, batteries, greeting cards')], default='OT', max_length=2),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='estoque_entrada_produto',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='estoque_saida_produto',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='fornecedor_nome',
            field=models.CharField(default='Fornecedor', max_length=200),
        ),
        migrations.AlterField(
            model_name='produto',
            name='produto_nome',
            field=models.CharField(default='Produto', max_length=200),
        ),
        migrations.AlterField(
            model_name='produto',
            name='produto_nome_vendedor',
            field=models.CharField(default='Vendedor', max_length=200),
        ),
        migrations.AlterField(
            model_name='produto',
            name='produto_venda_data',
            field=models.DateField(default=datetime.datetime(2021, 4, 20, 2, 37, 46, 186497, tzinfo=utc)),
        ),
    ]