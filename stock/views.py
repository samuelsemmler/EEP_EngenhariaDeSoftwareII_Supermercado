from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Produto
from .models import Estoque

# Create your views here.

@login_required
def sell_product(request, product_id):
    product = Produto.objects.filter(id=product_id).first()
    print(f'========================================= {product.produto_nome} =========================================')

    if request.method == 'POST':
        if product.produto_quantidade > 0:
            product.produto_quantidade -= 1

            stock = Estoque.objects.first()
            stock.estoque_total_produtos += 1
            stock.estoque_total_ativo_produtos -= 1
            stock.estoque_produtos_saida += 1

            product.save()
            stock.save()

            return redirect('products:products_list')
    
    context = {
        'product': product,
    }
    return render(request, 'stock/sell.html', context)
