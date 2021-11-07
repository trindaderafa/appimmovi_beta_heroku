from django.shortcuts import render
#from django.http import HttpResponse
from .models import (Pessoa,
                     Finalidade,
                     Diarista,
                     AtividadeDia,
                     Mensalista,
                     AtividadeMes,
                     Anualista,
                     AtividadeAno,
                     )

def home(request):
    context = {'mensagem': 'Ola mundo de novo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'usuario': pessoas})


def lista_finalidades(request):
    finalidade = Finalidade.objects.all()
    return render(request, 'core/lista_finalidades.html', {'finalidades': finalidade})


def lista_diaristas(request):
    diarista = Diarista.objects.all()
    return render(request, 'core/lista_diaristas.html', {'diaristas': diarista})


def lista_atividades_dia(request):
    atividade_dia = AtividadeDia.objects.all()
    return render(request, 'core/lista_atividades_dia.html', {'atividades_dia': atividade_dia})


def lista_mensalistas(request):
    mensalista = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalista})


def lista_atividades_mes(request):
    atividade_mes = AtividadeMes.objects.all()
    return render(request, 'core/lista_atividades_mes.html', {'atividades_mes': atividade_mes})


def lista_anualistas(request):
    anualista = Anualista.objects.all()
    return render(request, 'core/lista_anualistas.html', {'anualistas': anualista})


def lista_atividades_ano(request):
    atividade_ano = AtividadeAno.objects.all()
    return render(request, 'core/lista_atividades_ano.html', {'atividades_ano': atividade_ano})