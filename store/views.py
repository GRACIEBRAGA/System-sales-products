# from django.shortcuts import render

# Create your views here.


from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from store.models import Cliente, Estoque, Venda


class Homepage(TemplateView):
    template_name = 'homepage.html'


class Homestore(TemplateView):
    template_name = 'homestore.html'


class Clientelist(ListView):
    template_name = "clientelist.html"
    model = Cliente
    fields = '__all__'
    queryset = Cliente.objects.all()


class ClienteCreate(CreateView):
    template_name = "clientecreate.html"
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('store:clientelist')


class Estoquelist(ListView):
    template_name = "estoquelist.html"
    model = Estoque
    queryset = Estoque.objects.all()


class Estoquecreate(CreateView):
    template_name = "estoquecreate.html"
    model = Estoque
    fields = '__all__'
    context_object_name = object
    success_url = reverse_lazy('store:estoquelist')

class Vendalist(ListView):
    template_name = "vendalist.html"
    model = Venda
    queryset = Venda.objects.all()


class Vendacreate(CreateView):
    template_name = "vendacreate.html"
    model = Venda
    fields = '__all__'
    success_url = reverse_lazy('store:vendalist')