from django.shortcuts import render, redirect
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

from .forms import (PessoaForm,
                    FinalidadeForm,
                    DiaristaForm,
                    AtividadeDiaForm,
                    MensalistaForm,
                    AtividadeMesForm,
                    AnualistaForm,
                    AtividadeAnoForm,
                    )

def home(request):
    context = {'mensagem': 'Ola mundo de novo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'usuario': pessoas, 'forms':form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['forms'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)

def lista_finalidades(request):
    finalidade = Finalidade.objects.all()
    form = FinalidadeForm()
    data = {'finalidades': finalidade, 'forms':form}
    return render(request, 'core/lista_finalidades.html', data)


def finalidade_novo(request):
    form = FinalidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_finalidades')


def finalidade_update(request, id):
    data = {}
    finalidade = Finalidade.objects.get(id=id)
    form = FinalidadeForm(request.POST or None, instance=finalidade)
    data['finalidade'] = finalidade
    data['forms'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_finalidades')
    else:
        return render(request, 'core/update_finalidade.html', data)


def lista_diaristas(request):
    diarista = Diarista.objects.all()
    form = DiaristaForm()
    data = {'diaristas': diarista, 'forms':form}
    return render(request, 'core/lista_diaristas.html', data)


def diarista_novo(request):
    form = DiaristaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_diaristas')


def lista_atividades_dia(request):
    atividade_dia = AtividadeDia.objects.all()
    form = AtividadeDiaForm()
    data = {'atividades_dia': atividade_dia, 'forms':form}
    return render(request, 'core/lista_atividades_dia.html', data)


def atividade_dia_novo(request):
    form = AtividadeDiaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_atividades_dia')


def lista_mensalistas(request):
    mensalista = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalista, 'forms':form}
    return render(request, 'core/lista_mensalistas.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


def lista_atividades_mes(request):
    atividade_mes = AtividadeMes.objects.all()
    form = AtividadeMesForm()
    data = {'atividades_mes': atividade_mes, 'forms':form}
    return render(request, 'core/lista_atividades_mes.html', data)


def atividade_mes_novo(request):
    form = AtividadeMesForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_atividades_mes')


def lista_anualistas(request):
    anualista = Anualista.objects.all()
    form = AnualistaForm()
    data = {'anualistas': anualista, 'forms':form}
    return render(request, 'core/lista_anualistas.html', data)


def anualista_novo(request):
    form = AnualistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_anualistas')


def lista_atividades_ano(request):
    atividade_ano = AtividadeAno.objects.all()
    form = AtividadeAnoForm()
    data = {'atividades_ano': atividade_ano, 'forms':form}
    return render(request, 'core/lista_atividades_ano.html', data)


def atividade_ano_novo(request):
    form = AtividadeAnoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_atividades_ano')