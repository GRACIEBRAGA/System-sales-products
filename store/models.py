from django.db import models
#import models
#import args as args
#import kwargs as kwargs
# Create your models here.

FORMA_DE_PAGAMENTO_CHOICES = (
    ("CRÉDITO", "Crédito"),
    ("DEBITO", "Débito"),
    ("PIX", "pix"),
    ("DINHEIRO", "Dinheiro")
)

FECHAR_VENDA_CHOICES = (
    ("NOTA DE PEDIDO", "Nota de pedido"),
    ("NOTA FISCAL", "Nota fiscal")
)

VALOR_TOTAL_VENDAS_CHOICES = (
    ("DIARIO", "Diário"),
    ("SEMANAL", "Semanal"),
    ("QUINZENAL", "Quinzenal"),
    ("MENSAL", "Mensal")
)

ESTADO_CHOICES = (
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espirito Santo"),
    ("GO", "Goias"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piaui"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", " Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins")
)

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    cnpj_cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(null=False, unique=True)
    CEP = models.IntegerField(default=None)
    logradouro = models.CharField(max_length=100, default=None)
    numero = models.CharField(max_length=100, default=None)
    complemento = models.CharField(max_length=100, default=None)
    bairro = models.CharField(max_length=100, default=None)
    ESTADO = models.CharField(choices=ESTADO_CHOICES, null=False, max_length=20, default=None)
    cidade = models.CharField(max_length=100, default=None)

    def __init__(self, nome_cliente, cnpj_cpf, telefone, email, endereco, logradouro,  numero, complemento, bairro, ESTADO, cidade, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nome_cliente = nome_cliente
        self._cnpj_cpf = cnpj_cpf
        self._telefone = telefone
        self._email = email
        self._endereco = endereco
        self.CEP = CEP
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.ESTADO = ESTADO
        self.cidade = cidade

    def save(self, *args, **kwargs):
        nome_cliente()
        # super().save(*args, **kwargs)
        nome_cliente_else()

def __str__(self):
    return self.nome_cliente


class Estoque(models.Model):
    estoque_inicial = models.IntegerField(blank=True, null=True, default='DEFAULT VALUE')
    produto = models.CharField(max_length=100)
    NCM = models.IntegerField(default=None)
    marca_produto = models.CharField(max_length=200)
    codigo_produto = models.IntegerField(default=None)
    valor_custo = models.IntegerField(verbose_name=None)
    valor_venda = models.IntegerField(verbose_name=None)
    qtde_estoque = models.IntegerField(max_length=None)

    def __init__(self, produto, NCM, marca_produto, codigo_produto, valor_custo, valor_venda, qtde_estoque, estoque_inicial,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.estoque_inicial = estoque_inicial
        self.produto = produto
        self.NCM = NCM
        self.marca_produto = marca_produto
        self.codigo_produto = codigo_produto
        self.valor_custo = valor_custo
        self.valor_venda = valor_venda
        self.qtde_estoque = qtde_estoque

    class Meta:
        managed = False
        db_table = 'store_estoque'
       # unique_together = ('estoque_inicial', 'nome', 'NCM', 'marca_produto', 'codigo_produto', 'valor_custo', 'valor_venda')

    @property
    def __str__(self):
        print("Produto {} cadastrado com sucesso".format(estoque))

    def pesquisar_produto_estoque(self):
        produto = input('Insira o nome do produto em letra minuscula')
        if 'produto' not in produtos:
            print('{} nao existe no estoque'.format(produto))
        else:
            i = produtos.index(produto)
            qtde_estoque = estoque[i]
            print('Temos {} unidades de {} no estoque'.format(qtde_estoque, produto))

    def save(self, *args, **kwargs):
        nome_estoque()
        super().save(*args, **kwargs)
        nome_estoque_else()


class Venda(models.Model):

    def __init__(self, abrir_caixa, nome_produto, codigo_produto, valor, desconto, valor_total, nome_cliente, cnpj_cpf_cliente, forma_de_pagamento, fechar_venda, fechar_caixa, valor_total_vendas, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.abrir_caixa = abrir_caixa
        self.nome_produto = nome_produto
        self.codigo_produto = codigo_produto
        self.valor = valor
        self.desconto = desconto
        self.valor_total = valor_total
        self.nome_cliente = nome_cliente
        self.cnpj_cpf_cliente = cnpj_cpf_cliente
        self.forma_de_pagamento = forma_de_pagamento
        self.fechar_venda = fechar_venda
        self.fechar_caixa = fechar_caixa
        self.valor_total_vendas = valor_total_vendas

    def abrir_caixa(self):
        abrir_caixa = input('Digite o valor inicial do caixa')
        return abrir_caixa

       # super().__init__(*args, **kwargs)

    def iniciar_venda(self):

        Vendas = []

        Caracter = dict[int, str, float]
        # mercadorias: [Caracter] = {"COD": "CD", "PROD": "DESC", "UN": "qtde", "PC": "VLUNIT", "Valor": "VTotal"}
        # Cliente: [Caracter] = {" Cliente": ":", }
        mercadorias: [Caracter] = {"codigo": ":", "produto": ':', "quant": ":", "Valor": ":", "VTotal": ":"}

        Vendas.append(mercadorias)

        cnpj_cpf = [int, float]
        cnpj_cpf = 0
        valor_geral = 0
        Desconto = 0
        subtotal = 0
        a = 1
        nome_cliente = 0

        while a < 2:
            C = int(input('Digite o codigo do produto'))
            P = input('Digite o nome do produto?')
            Q = float(input('Digite a qtde'))
            VU = float(input('Digite o valor unitário'))
            VT = (Q * VU)
            valor_geral = (VT + valor_geral)  # o sale1 é a soma total dos produto
            mercadorias = {"Cod": C, "Prod": P, "qtde": Q, "Valor_unt": VU, "valor_total": VT}
            Vendas.append(mercadorias)
            Desconto = float(input("Digite o valor do desconto"))
            subtotal = (valor_geral - Desconto)
            if Desconto > 1:
                print(subtotal)
            else:
                pass

            g = int(input('digite 1 para continuar ou qualquer tecla'))
            if g < 2:
                a = 1
            else:
                print('-' * 50)
                print("loja magazine luiza ltda")
                print('CNPJ : 141231230001/01')
                print('ruas da camelias, 25, centro, sao luis, ma')
                print('-' * 50)

                print('=' * 50)
                nome_cliente = input('Cliente: ')
                cnpj_cpf = input(' CNPJ ou CPF: ')
                print('=' * 50)

                for mercadorias in Vendas:
                    print(mercadorias)
                    a = 2

        print('=' * 50)
        print("Valor total R$ %.2f" % (valor_geral))
        print("desconto R$ %.2f" % (Desconto))
        print("subtotal R$ %.2f" % (subtotal))
        print(f"Valor total das compras = R$ %.2f" % (subtotal))
        print('=' * 50)
    @property
    def __str__(self):
        return self.Venda


    @property
    def __init__(self, fechar_caixa=0):
        self.fechar_caixa = fechar_caixa
        # super().__init__(*args, **kwargs)
        print('Valor total de vendas do dia foi de: R$ {}'.format(Venda))

    def save(self, *args, **kwargs):
        nome_venda()
        super().save(*args, **kwargs)
        nome_venda_else()


class NotaFiscal(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.NotaFiscal = 0
        self.method = 0

    def upload_file(request):
        if request.method == 'POST':
            form = ModelFormWithFileField()
            if form.is_valid():
                # file is saved
                form.save(NotaFiscal)
                return HttpResponseRedirect('/success/url/')
        else:
            form = ModelFormWithFileField()
        return render(request, 'upload.html', {'form': form})

    def __str__(self):
        return self.NotaFiscal