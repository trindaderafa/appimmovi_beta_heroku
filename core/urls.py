from django.urls import include, path
from .views import (home,
                    lista_pessoas,
                    lista_finalidades,
                    lista_diaristas,
                    lista_atividades_dia,
                    lista_diaristas,
                    lista_mensalistas,
                    lista_atividades_mes,
                    lista_anualistas,
                    lista_atividades_ano,
                    )


urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('finalidades/', lista_finalidades, name='core_lista_finalidades'),
    path('diaristas/', lista_diaristas, name='core_lista_diaristas'),
    path('atividades_dia/', lista_atividades_dia, name='core_lista_atividades_dia'),
    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('atividades_mes/', lista_atividades_mes, name='core_lista_atividades_mes'),
    path('anualistas/', lista_anualistas, name='core_lista_anualistas'),
    path('atividades_ano/', lista_atividades_ano, name='core_lista_atividades_ano'),
]