from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from PIL import Image

# Create your models here.


class Profile(models.Model):
    class ProfileType(models.TextChoices):
        SUPERVISOR = 'SU', _('Supervisor')
        CASHIER = 'CA', _('Caixa')

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    usuario_imagem = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    usuario_status = models.CharField(max_length=2, choices=ProfileType.choices, default=ProfileType.CASHIER)
    usuario_data_criacao = models.DateField(auto_now_add=True)
    usuario_primeiro_nome = models.CharField(max_length=200, default='first name')
    usuario_ultimo_nome = models.CharField(max_length=200, default='last name')
    usuario_rua = models.CharField(max_length=200, default='street')
    usuario_cidade = models.CharField(max_length=200, default='city')
    usuario_estado = models.CharField(max_length=200, default='state')
    usuario_pais = models.CharField(max_length=200, default='country')
    usuario_telefone_fixo = models.CharField(max_length=200, default='+55 000 11111111111')
    usuario_telefone_movel = models.CharField(max_length=200, default='+55 000 11111111111')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.usuario_imagem.path)

        img_modified = img.convert('RGB')

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img_modified.thumbnail(output_size)
            img_modified.save(self.usuario_imagem.path)