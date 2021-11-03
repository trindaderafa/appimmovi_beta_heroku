from django.shortcuts import render
#from django.http import HttpResponse
from .models import Pessoa

def home(request):
    context = {'mensagem': 'Ola mundo de novo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'usuario': pessoas})
