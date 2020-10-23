from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
from django.template import loader


def index(request):
    lista_de_clientes = Cliente.objects.all()
    context = {
        'lista_de_clientes': lista_de_clientes,
    }
    return render(request, 'banco/index.html', context)
