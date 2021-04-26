from products.models import Produto
from suppliers.models import Fornecedor

suppliers = Fornecedor.objects.all()

counter = 0
for i in suppliers:
    product = Produto(
        produto_nome=f'Refrigerante {counter}',
        produto_tipo='BE',
        produto_preco=3.50,
        produto_quantidade=2,
        produto_nome_vendedor='Jurisclayton',
    )
    product.save()
    product.fornecedor_pk.add(i)
    product.save()

    counter += 1

# exec(open("products/products_database_injection.py").read())