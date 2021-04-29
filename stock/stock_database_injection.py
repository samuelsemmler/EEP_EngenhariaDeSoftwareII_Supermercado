from stock.models import Estoque
from products.models import Produto

product = Produto.objects.all()
stock = Estoque.objects.first()

for i in product:
    stock.produto_pk.add(i) 
    stock.save()

# exec(open("stock/stock_database_injection.py").read())
