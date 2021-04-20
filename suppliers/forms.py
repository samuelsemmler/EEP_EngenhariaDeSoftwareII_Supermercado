from django import forms
from .models import Fornecedor


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['fornecedor_nome', 'fornecedor_nome_empresa', 'fornecedor_email', 'fornecedor_endereco', 'fornecedor_cidade', 'fornecedor_pais', 'fornecedor_comentarios']