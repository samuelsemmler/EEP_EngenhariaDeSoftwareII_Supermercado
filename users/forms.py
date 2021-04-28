from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['usuario_imagem', 'usuario_primeiro_nome', 'usuario_ultimo_nome', 'usuario_rua', 'usuario_cidade', 'usuario_estado', 'usuario_pais', 'usuario_telefone_fixo', 'usuario_telefone_movel']
