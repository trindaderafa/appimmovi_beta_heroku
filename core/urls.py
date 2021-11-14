from django.urls import include, path
from .views import (home,
                    lista_pessoas,
                    lista_finalidades,
                    lista_diaristas,
                    lista_atividades_dia,
                    lista_mensalistas,
                    lista_atividades_mes,
                    lista_anualistas,
                    lista_atividades_ano,
                    lista_vitalistas,
                    lista_atividades_vital,
                    pessoa_novo,
                    finalidade_novo,
                    diarista_novo,
                    atividade_dia_novo,
                    mensalista_novo,
                    atividade_mes_novo,
                    anualista_novo,
                    atividade_ano_novo,
                    vitalista_novo,
                    atividade_vital_novo,
                    pessoa_update,
                    finalidade_update,
                    diarista_update,
                    atividade_dia_update,
                    mensalista_update,
                    atividade_mes_update,
                    anualista_update,
                    atividade_ano_update,
                    vitalista_update,
                    atividade_vital_update,
                    pessoa_delete,
                    )


urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa_update/<int:id>/', pessoa_update, name='core_pessoa_update'),
    path('pessoa_delete/<int:id>/', pessoa_delete, name='core_pessoa_delete'),

    path('finalidades/', lista_finalidades, name='core_lista_finalidades'),
    path('finalidade_novo/', finalidade_novo, name='core_finalidade_novo'),
    path('finalidade_update/<int:id>/', finalidade_update, name='core_finalidade_update'),

    path('diaristas/', lista_diaristas, name='core_lista_diaristas'),
    path('diarista_novo/', diarista_novo, name='core_diarista_novo'),
    path('diarista_update/<int:id>/', diarista_update, name='core_diarista_update'),

    path('atividades_dia/', lista_atividades_dia, name='core_lista_atividades_dia'),
    path('atividade_dia_novo/', atividade_dia_novo, name='core_atividade_dia_novo'),
    path('atividade_dia_update/<int:id>/', atividade_dia_update, name='core_atividade_dia_update'),

    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalista_novo/', mensalista_novo, name='core_mensalista_novo'),
    path('mensalista_update/<int:id>/', mensalista_update, name='core_mensalista_update'),

    path('atividades_mes/', lista_atividades_mes, name='core_lista_atividades_mes'),
    path('atividade_mes_novo/', atividade_mes_novo, name='core_atividade_mes_novo'),
    path('atividade_mes_update/<int:id>/', atividade_mes_update, name='core_atividade_mes_update'),

    path('anualistas/', lista_anualistas, name='core_lista_anualistas'),
    path('anualista_novo/', anualista_novo, name='core_anualista_novo'),
    path('anualista_update/<int:id>/', anualista_update, name='core_anualista_update'),

    path('atividades_ano/', lista_atividades_ano, name='core_lista_atividades_ano'),
    path('atividade_ano_novo/', atividade_ano_novo, name='core_atividade_ano_novo'),
    path('atividade_ano_update/<int:id>/', atividade_ano_update, name='core_atividade_ano_update'),

    path('vitalistas/', lista_vitalistas, name='core_lista_vitalistas'),
    path('vitalista_novo/', vitalista_novo, name='core_vitalista_novo'),
    path('vitalista_update/<int:id>/', vitalista_update, name='core_vitalista_update'),

    path('atividades_vital/', lista_atividades_vital, name='core_lista_atividades_vital'),
    path('atividade_vital_novo/', atividade_vital_novo, name='core_atividade_vital_novo'),
    path('atividade_vital_update/<int:id>/', atividade_vital_update, name='core_atividade_vital_update'),
]