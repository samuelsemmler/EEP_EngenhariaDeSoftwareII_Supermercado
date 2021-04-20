from django import forms
from .models import Produto
from suppliers.models import Fornecedor


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['produto_nome', 'produto_tipo', 'produto_preco', 'produto_quantidade', 'produto_nome_vendedor', 'fornecedor_pk']
