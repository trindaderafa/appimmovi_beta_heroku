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
                     Vitalista,
                     AtividadeVital,
                     )

from .forms import (PessoaForm,
                    FinalidadeForm,
                    DiaristaForm,
                    AtividadeDiaForm,
                    MensalistaForm,
                    AtividadeMesForm,
                    AnualistaForm,
                    AtividadeAnoForm,
                    VitalistaForm,
                    AtividadeVitalForm,
                    )

def home(request):
    return render(request, 'core/index.html')


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


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':pessoa})


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


def finalidade_delete(request, id):
    finalidade = Finalidade.objects.get(id=id)
    if request.method == 'POST':
        finalidade.delete()
        return redirect('core_lista_finalidades')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':finalidade})


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


def diarista_update(request, id):
    data = {}
    diarista = Diarista.objects.get(id=id)
    form = DiaristaForm(request.POST or None, instance=diarista)
    data['diarista'] = diarista
    data['forms'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_diaristas')
    else:
        return render(request, 'core/update_diarista.html', data)


def diarista_delete(request, id):
    diarista = Diarista.objects.get(id=id)
    if request.method == 'POST':
        diarista.delete()
        return redirect('core_lista_diaristas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':diarista})


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


def atividade_dia_update(request, id):
    data = {}
    atividade_dia = AtividadeDia.objects.get(id=id)
    form = AtividadeDiaForm(request.POST or None, instance=atividade_dia)
    data['atividade_dia'] = atividade_dia
    data['forms'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_atividades_dia')
    else:
        return render(request, 'core/update_atividade_dia.html', data)


def atividade_dia_delete(request, id):
    atividade_dia = AtividadeDia.objects.get(id=id)
    if request.method == 'POST':
        atividade_dia.delete()
        return redirect('core_lista_atividades_dia')
    else:
        return render(request, 'core/delete_confirm.html',
                      {'obj':atividade_dia})


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


def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['forms'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)


def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':mensalista})


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


def atividade_mes_update(request, id):
    data = {}
    atividade_mes = AtividadeMes.objects.get(id=id)
    form = AtividadeMesForm(request.POST or None, instance=atividade_mes)
    data['atividade_mes'] = atividade_mes
    data['forms'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_atividades_mes')
    else:
        return render(request, 'core/update_atividade_mes.html', data)


def atividade_mes_delete(request, id):
    atividade_mes = AtividadeMes.objects.get(id=id)
    if request.method == 'POST':
        atividade_mes.delete()
        return redirect('core_lista_atividades_mes')
    else:
        return render(request, 'core/delete_confirm.html',
                      {'obj':atividade_mes})


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


def anualista_update(request, id):
    data = {}
    anualista = Anualista.objects.get(id=id)
    form = AnualistaForm(request.POST or None, instance=anualista)
    data['anualista'] = anualista
    data['forms'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_anualistas')
    else:
        return render(request, 'core/update_anualista.html', data)


def anualista_delete(request, id):
    anualista = Anualista.objects.get(id=id)
    if request.method == 'POST':
        anualista.delete()
        return redirect('core_lista_anualistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':anualista})


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


def atividade_ano_update(request, id):
    data = {}
    atividade_ano = AtividadeAno.objects.get(id=id)
    form = AtividadeAnoForm(request.POST or None, instance=atividade_ano)
    data['atividade_ano'] = atividade_ano
    data['forms'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_atividades_ano')
    else:
        return render(request, 'core/update_atividade_ano.html', data)


def atividade_ano_delete(request, id):
    atividade_ano = AtividadeAno.objects.get(id=id)
    if request.method == 'POST':
        atividade_ano.delete()
        return redirect('core_lista_atividades_ano')
    else:
        return render(request, 'core/delete_confirm.html',
                      {'obj':atividade_ano})


def lista_vitalistas(request):
    vitalista = Vitalista.objects.all()
    form = VitalistaForm()
    data = {'vitalistas': vitalista, 'forms':form}
    return render(request, 'core/lista_vitalistas.html', data)


def vitalista_novo(request):
    form = VitalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_vitalistas')


def vitalista_update(request, id):
    data = {}
    vitalista = Vitalista.objects.get(id=id)
    form = VitalistaForm(request.POST or None, instance=vitalista)
    data['vitalista'] = vitalista
    data['forms'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_vitalistas')
    else:
        return render(request, 'core/update_vitalista.html', data)


def vitalista_delete(request, id):
    vitalista = Vitalista.objects.get(id=id)
    if request.method == 'POST':
        vitalista.delete()
        return redirect('core_lista_vitalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':vitalista})


def lista_atividades_vital(request):
    atividade_vital = AtividadeVital.objects.all()
    form = AtividadeVitalForm()
    data = {'atividades_vital': atividade_vital, 'forms':form}
    return render(request, 'core/lista_atividades_vital.html', data)


def atividade_vital_novo(request):
    form = AtividadeVitalForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_atividades_vital')


def atividade_vital_update(request, id):
    data = {}
    atividade_vital = AtividadeVital.objects.get(id=id)
    form = AtividadeVitalForm(request.POST or None, instance=atividade_vital)
    data['atividade_vital'] = atividade_vital
    data['forms'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_atividades_vital')
    else:
        return render(request, 'core/update_atividade_vital.html', data)


def atividade_vital_delete(request, id):
    atividade_vital = AtividadeVital.objects.get(id=id)
    if request.method == 'POST':
        atividade_vital.delete()
        return redirect('core_lista_atividades_vital')
    else:
        return render(request, 'core/delete_confirm.html',
                      {'obj':atividade_vital})


