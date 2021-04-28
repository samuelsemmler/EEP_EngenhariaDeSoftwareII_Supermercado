from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Fornecedor
from .forms import FornecedorForm

# Create your views here.


@login_required
def suppliers_list(request):
    supplier = Fornecedor.objects.all()

    context = {
        'supplier': supplier
    }

    return render(request, 'suppliers/index.html', context)


@login_required
def supplier_detail(request, supplier_id):
    supplier = Fornecedor.objects.get(id=supplier_id)

    context = {
        'supplier': supplier
    }

    return render(request, 'suppliers/details.html', context)


@login_required
def supplier_add(request):
    form = FornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('suppliers:suppliers_list')

    context = {
        'form': form
    }
    return render(request, 'suppliers/form.html', context)


@login_required
def supplier_update(request, supplier_id):
    supplier = Fornecedor.objects.get(id=supplier_id)
    form = FornecedorForm(request.POST or None, instance=supplier)

    if form.is_valid():
        form.save()
        return redirect('suppliers:suppliers_list')

    context = {
        'form': form,
        'supplier': supplier,
    }
    return render(request, 'suppliers/form.html', context)


@login_required
def supplier_remove(request, supplier_id):
    supplier = Fornecedor.objects.get(id=supplier_id)

    if request.method == 'POST':
        supplier.delete()
        return redirect('suppliers:suppliers_list')
    
    context = {
        'supplier': supplier
    }
    return render(request, 'suppliers/delete.html', context)
    
