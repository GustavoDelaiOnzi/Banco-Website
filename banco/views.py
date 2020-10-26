from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Conta, Transacao
from django.template import loader
from datetime import date
from dateutil.relativedelta import relativedelta

def index(request):
    lista_de_clientes = Cliente.objects.all() #Lista de todos os clientes
    context = {
        'lista_de_clientes': lista_de_clientes,
    }
    return render(request, 'banco/index.html', context)

def detail(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id) #Conta selecionada
    except Cliente.DoesNotExist:
        raise Http404("Cliente does not exist")
    return render(request, 'banco/detail.html', {'cliente': cliente})


def conta(request, conta_id):
    try:
        conta = Conta.objects.get(pk=conta_id) #Conta selecionada
        lista_de_trancaoes = Transacao.objects.filter(conta=conta_id) #lista de todas as transações da conta selecionada
        soma_de_preco = 0

        for transacao in lista_de_trancaoes:
            if transacao.horario < date.today() - relativedelta(months=+1): #Exclui da lista todas as transações que tem mais de 30 dias
                lista_de_trancaoes = lista_de_trancaoes.exclude(nome=transacao.nome)
            soma_de_preco += transacao.valor #calcula o saldo antes do 30 dias

        saldo_inicial = conta.saldo - soma_de_preco
        transacoes_debito = lista_de_trancaoes.filter(metodo="D") #filtragem das transações de metodo débito
        transacoes_credito = lista_de_trancaoes.filter(metodo="C") #filtragem das transações de metodo crédito
    except Cliente.DoesNotExist:
        raise Http404("Conta does not exist")
    context = {
        'conta': conta,
        'lista_de_trancaoes': lista_de_trancaoes, #lista de todas as transações da conta selecionada que estão no prazo de 30 dias
        'saldo_inicial': saldo_inicial, #saldo antes dos 30 dias
        'transacoes_debito': transacoes_debito, #lista de todas as transações com o metodo = debito
        'transacoes_credito': transacoes_credito, #lista de todas as transações com o metodo = credito
    }
    return render(request, 'banco/conta.html', context)
