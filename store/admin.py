from django.contrib import admin
from store.models import Cliente, Estoque, Venda
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Estoque)
admin.site.register(Venda)
