from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    class ProfileTipos(models.TextChoices):
        SUPERVISOR = 'SU', _('Nível Supervisor')
        CAIXA = 'CA', _('Nível Gerente')
        

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=ProfileTipos.choices, default=ProfileTipos.CAIXA)

    def __str__(self) -> str:
        return self.user.username