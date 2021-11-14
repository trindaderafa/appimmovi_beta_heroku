from django.contrib import admin
from .models import (Pessoa,
                     Finalidade,
                     Parametro,
                     Diarista,
                     AtividadeDia,
                     Mensalista,
                     AtividadeMes,
                     Anualista,
                     AtividadeAno,
                     Vitalista,
                     AtividadeVital,
                     )


class AtividadeDiaAdmin(admin.ModelAdmin):
    list_display = ('diarista',
                    'finalidade',
                    'inicio_dia',
                    'valor_dia',
                    'dias_total',
                    'valor_total',
                    'pago'
                    )


class AtividadeMesAdmin(admin.ModelAdmin):
    list_display = ('mensalista',
                    'finalidade',
                    'inicio_mes',
                    'valor_mes',
                    'dias_total',
                    'valor_total',
                    'pago'
                    )



class AtividadeAnoAdmin(admin.ModelAdmin):
    list_display = ('anualista',
                    'finalidade',
                    'inicio_ano',
                    'valor_ano',
                    'dias_total',
                    'valor_total',
                    'pago'
                    )


class AtividadeVitalAdmin(admin.ModelAdmin):
    list_display = ('vitalista',
                    'finalidade',
                    'inicio_ano',
                    'valor',
                    'dias_total',
                    'valor_total',
                    'pago'
                    )

admin.site.register(Pessoa)
admin.site.register(Finalidade)
admin.site.register(Parametro)
admin.site.register(Diarista)
admin.site.register(AtividadeDia, AtividadeDiaAdmin)
admin.site.register(Mensalista)
admin.site.register(AtividadeMes, AtividadeMesAdmin)
admin.site.register(Anualista)
admin.site.register(AtividadeAno, AtividadeAnoAdmin)
admin.site.register(Vitalista)
admin.site.register(AtividadeVital, AtividadeVitalAdmin)


