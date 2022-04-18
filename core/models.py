from django.db import models
import math


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    profissao = models.CharField(max_length=100)
    area_atuacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Finalidade(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Parametro(models.Model):
    valor_dia = models.DecimalField(max_digits=4, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=5, decimal_places=2)
    valor_ano = models.DecimalField(max_digits=6, decimal_places=2)
    valor_licenca = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return 'Parametros de Atividade'


class Diarista(models.Model):
    usuario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    inicio = models.DateTimeField(auto_now=False)
    termino = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.usuario)


class AtividadeDia(models.Model):
    diarista = models.ForeignKey(Diarista, on_delete=models.CASCADE)
    finalidade = models.ForeignKey(Finalidade, on_delete=models.CASCADE, verbose_name='serviço')
    valor_dia = models.DecimalField(max_digits=4, decimal_places=2)
    pago = models.BooleanField(default=False)

    def dias_total(self):
        return math.ceil(((self.diarista.termino - self.diarista.inicio).total_seconds() / 86400)-1)

    def inicio_dia(self):
        return self.diarista.inicio

    def valor_total(self):
        return self.valor_dia * self.dias_total()

    def __str__(self):
        return str(self.finalidade.nome) + ' - ' + str(self.diarista.usuario)


class Mensalista(models.Model):
    usuario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    inicio = models.DateTimeField(auto_now=False)
    termino = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.usuario)# + ' - ' + str(self.inicio)


class AtividadeMes(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    finalidade = models.ForeignKey(Finalidade, on_delete=models.CASCADE, verbose_name='serviço')
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)
    pago = models.BooleanField(default=False)

    def dias_total(self):
        return math.ceil(((self.mensalista.termino - self.mensalista.inicio).total_seconds() / 86400)-1)

    def mes_total(self):
        return round(self.dias_total()/30, 2)

    def valor_total(self):
        return round(self.valor_mes * self.dias_total()/30, 2)

    def inicio_mes(self):
        return self.mensalista.inicio

    def __str__(self):
        return str(self.finalidade.nome) + ' - ' + str(self.mensalista.usuario)


class Anualista(models.Model):
    usuario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    inicio = models.DateTimeField(auto_now=False)
    termino = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.usuario)# + ' - ' + str(self.inicio)


class AtividadeAno(models.Model):
    anualista = models.ForeignKey(Anualista, on_delete=models.CASCADE)
    finalidade = models.ForeignKey(Finalidade, on_delete=models.CASCADE, verbose_name='serviço')
    valor_ano = models.DecimalField(max_digits=6, decimal_places=2)
    pago = models.BooleanField(default=False)

    def dias_total(self):
        return math.ceil(((self.anualista.termino - self.anualista.inicio).total_seconds() / 86400) - 1)

    def anos_total(self):
        return round(self.dias_total() / 365, 2)

    def inicio_ano(self):
        return self.anualista.inicio

    def valor_total(self):
        return round(self.valor_ano * self.dias_total()/365, 2)

    def __str__(self):
        return str(self.finalidade.nome) + ' - ' + str(self.anualista.usuario)


class Vitalista(models.Model):
    usuario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    inicio = models.DateTimeField(auto_now=False)
    termino = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.usuario)


class AtividadeVital(models.Model):
    vitalista = models.ForeignKey(Vitalista, on_delete=models.CASCADE)
    finalidade = models.ForeignKey(Finalidade, on_delete=models.CASCADE, verbose_name='serviço')
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    pago = models.BooleanField(default=False)

    def dias_total(self):
        return math.ceil(((self.vitalista.termino - self.vitalista.inicio).total_seconds() / 86400) - 1)

    def inicio(self):
        return self.vitalista.inicio

    def anos_total(self):
        return round(self.dias_total() / 365, 2)

    def __str__(self):
        return str(self.finalidade.nome) + ' - ' + str(self.vitalista.usuario)
