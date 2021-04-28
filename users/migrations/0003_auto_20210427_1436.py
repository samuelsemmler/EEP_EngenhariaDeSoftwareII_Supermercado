# Generated by Django 3.2 on 2021-04-27 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='usuario_imagem',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='status',
            new_name='usuario_status',
        ),
        migrations.AddField(
            model_name='profile',
            name='usuario_cidade',
            field=models.CharField(default='city', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='usuario_data_criacao',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='usuario_estado',
            field=models.CharField(default='state', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='usuario_pais',
            field=models.CharField(default='country', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='usuario_primeiro_nome',
            field=models.CharField(default='first name', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='usuario_rua',
            field=models.CharField(default='street', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='usuario_ultimo_nome',
            field=models.CharField(default='last name', max_length=200),
        ),
    ]