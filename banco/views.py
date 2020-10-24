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

def detail(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        raise Http404("Cliente does not exist")
    return render(request, 'banco/detail.html', {'cliente': cliente})
