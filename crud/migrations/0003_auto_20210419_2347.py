# Generated by Django 3.2 on 2021-04-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20210419_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='fornecedor_comentarios',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='fornecedor_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='fornecedor_endereco',
            field=models.CharField(default='Localization', max_length=200),
        ),
        migrations.AlterField(
            model_name='produto',
            name='produto_venda_data',
            field=models.DateField(auto_now_add=True),
        ),
    ]
