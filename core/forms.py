from django.forms import ModelForm
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

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class FinalidadeForm(ModelForm):
    class Meta:
        model = Finalidade
        fields = '__all__'


class DiaristaForm(ModelForm):
    class Meta:
        model = Diarista
        fields = '__all__'


class AtividadeDiaForm(ModelForm):
    class Meta:
        model = AtividadeDia
        fields = '__all__'


class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'


class AtividadeMesForm(ModelForm):
    class Meta:
        model = AtividadeMes
        fields = '__all__'


class AnualistaForm(ModelForm):
    class Meta:
        model = Anualista
        fields = '__all__'


class AtividadeAnoForm(ModelForm):
    class Meta:
        model = AtividadeAno
        fields = '__all__'


class VitalistaForm(ModelForm):
    class Meta:
        model = Vitalista
        fields = '__all__'


class AtividadeVitalForm(ModelForm):
    class Meta:
        model = AtividadeVital
        fields = '__all__'