from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=40)
    sexo = models.CharField(max_length=1)
    def __str__(self):
        return self.nome


class Conta(models.Model):
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    numero_do_cartao = models.CharField(max_length=16)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return "Conta: " + str(self.id)

class Transacao(models.Model):
    nome = models.CharField(max_length=40)
    empresa = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=1)
    descricao = models.CharField(max_length=40)
    horario = models.DateField('date published')
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome