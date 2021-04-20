from products.models import Produto
from suppliers.models import Fornecedor

supplier = Fornecedor.objects.last()

product = Produto(
    produto_nome='Refrigerante',
    produto_tipo='BE',
    produto_preco=3.50,
    produto_quantidade=2,
    produto_nome_vendedor='Jurisclayton',
)
product.save()
product.fornecedor_pk.add(supplier)
product.save()

# exec(open("products/products_database_injection.py").read())