from django import forms
from store.models import Cliente, Estoque, Venda, NotaFiscal


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = "__all__"

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = "__all__"

class NotaFiscalForm(forms.ModelForm):
    class Meta:
        model = NotaFiscal
        fields = "__all__"

