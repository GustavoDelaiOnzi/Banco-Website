from django.contrib import admin

from .models import Cliente, Conta, Transacao

admin.site.register(Cliente)
admin.site.register(Conta)
admin.site.register(Transacao)

