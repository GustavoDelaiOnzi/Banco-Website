from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Conta, Transacao
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

def conta(request, conta_id):
    try:
        conta = Conta.objects.get(pk=conta_id)
        lista_de_trancaoes = Transacao.objects.all()
        soma_de_preco = 0
        for transacao in lista_de_trancaoes:
            soma_de_preco += transacao.valor
        saldo_inicial = conta.saldo + soma_de_preco
    except Cliente.DoesNotExist:
        raise Http404("Conta does not exist")
    context = {
        'conta': conta,
        'lista_de_trancaoes': lista_de_trancaoes,
        'saldo_inicial': saldo_inicial,
    }
    return render(request, 'banco/conta.html', context)
