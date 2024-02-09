from django.db import models
from django.utils import timezone

# Create your models here.
class Pedido(models.Model):
    data_entrada = models.DateTimeField(default=timezone.now)
    nfe = models.CharField(max_length = 10)
    op = models.CharField(max_length = 10)
    material = models.CharField(max_lengrh = 10)
    class Tipo(models.IntegerChoices):
        M = 0
        J = 1
        T = 2
    tipo = models.IntegerField(choices = Tipo)
    cliente = models.CharField(max_length = 75)
    tempo_de_confeccao = models.FloatField()
    vl_peca = models.DecimalField(decimal_places = 2)
    vl_frete_pc = models.DecimalField(decimal_places = 2)
    vl_frete_e = models.DecimalField(decimal_places = 2)
    qtd_entrada = models.IntegerField()
    faturamento_a_receber = models.DecimalField(decimal_places = 2)
    nf_ret = models.CharField()
    qtd_pecas_retorno = models.IntegerField()
    total = models.DecimalField(decimal_places = 2)
    vl_recebido = models.BooleanField(default=False)
    data_pagamento = models.DateField(blank=True, null=True)
    tempo_entrada = models.FloatField()
    artok_e = models.IntegerField()
    tempo_retorno = models.FloatField()
    artok_r = models.IntegerField()
    aliquota = models.FloatField()
    data_vencimento_pagamento = models.DateField()
    