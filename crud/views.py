from django.shortcuts import render
from .models import Estoque, Produto

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def users(request):
    return render(request, 'users.html', {})


