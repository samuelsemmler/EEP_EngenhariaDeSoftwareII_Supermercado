from django.shortcuts import redirect, render
from .models import Fornecedor
from .forms import FornecedorForm

# Create your views here.


def suppliers_list(request):
    supplier = Fornecedor.objects.all()

    context = {
        'supplier': supplier
    }

    return render(request, 'supplier-list.html', context)


def supplier_detail(request, supplier_id):
    supplier = Fornecedor.objects.get(id=supplier_id)

    context = {
        'supplier': supplier
    }

    return render(request, 'supplier-details.html', context)


def supplier_add(request):
    form = FornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('suppliers:suppliers_list')

    context = {
        'form': form
    }
    return render(request, 'supplier-form.html', context)


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
    return render(request, 'supplier-form.html', context)


def supplier_remove(request, supplier_id):
    supplier = Fornecedor.objects.get(id=supplier_id)

    if request.method == 'POST':
        supplier.delete()
        return redirect('suppliers:suppliers_list')
    
    context = {
        'supplier': supplier
    }
    return render(request, 'supplier-delete.html', context)
    
