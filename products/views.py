from products.forms import ProdutoForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Produto
from suppliers.models import Fornecedor

# Create your views here.

@login_required
def products_list(request):
    product = Produto.objects.all()
    higher = 0
    suppliers = []
    for i in product:
        suppliers.append(Fornecedor.objects.filter(produto=i))
        if i.fornecedor_pk.count() > higher:
            higher = i.fornecedor_pk.count()
    
    context = {
        'data': zip(product, suppliers),
        'higher': range(higher),
    }
    return render(request, 'products/index.html', context)


@login_required
def product_add(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products:products_list')

    context = {
        'form': form
    }
    return render(request, 'products/form.html', context)


@login_required
def product_details(request, product_id):
    product = Produto.objects.filter(id=product_id)
    suppliers = []
    for i in product:
        suppliers.append(Fornecedor.objects.filter(produto=i))
    
    context = {
        'data': zip(product, suppliers),
    }
    return render(request, 'products/details.html', context)


@login_required
def product_update(request, product_id):
    product = Produto.objects.filter(id=product_id).first()
    form = ProdutoForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('products:products_list')

    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'products/form.html', context)


@login_required
def product_remove(request, product_id):
    product = Produto.objects.filter(id=product_id).first()

    if request.method == 'POST':
        product.delete()
        return redirect('products:products_list')
    
    context = {
        'product': product
    }
    return render(request, 'products/delete.html', context)