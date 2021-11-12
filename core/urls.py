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
                    pessoa_novo,
                    finalidade_novo,
                    diarista_novo,
                    atividade_dia_novo,
                    mensalista_novo,
                    atividade_mes_novo,
                    anualista_novo,
                    atividade_ano_novo,
                    pessoa_update,
                    finalidade_update,
                    )


urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa_update/<int:id>/', pessoa_update, name='core_pessoa_update'),

    path('finalidades/', lista_finalidades, name='core_lista_finalidades'),
    path('finalidade_novo/', finalidade_novo, name='core_finalidade_novo'),
    path('finalidade_update/<int:id>/', finalidade_update, name='core_finalidade_update'),

    path('diaristas/', lista_diaristas, name='core_lista_diaristas'),
    path('diarista_novo/', diarista_novo, name='core_diarista_novo'),

    path('atividades_dia/', lista_atividades_dia, name='core_lista_atividades_dia'),
    path('atividade_dia_novo/', atividade_dia_novo, name='core_atividade_dia_novo'),

    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalista_novo/', mensalista_novo, name='core_mensalista_novo'),

    path('atividades_mes/', lista_atividades_mes, name='core_lista_atividades_mes'),
    path('atividade_mes_novo/', atividade_mes_novo, name='core_atividade_mes_novo'),

    path('anualistas/', lista_anualistas, name='core_lista_anualistas'),
    path('anualista_novo/', anualista_novo, name='core_anualista_novo'),

    path('atividades_ano/', lista_atividades_ano, name='core_lista_atividades_ano'),
    path('atividade_ano_novo/', atividade_ano_novo, name='core_atividade_ano_novo'),
]