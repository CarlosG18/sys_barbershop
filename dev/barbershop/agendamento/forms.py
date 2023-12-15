from django import forms
from .models import Servico, Agendamento,Servico_Agendamento

class FormService(forms.ModelForm):
    class Meta:
        model = Servico
        exclude = ['id']

class FormServico_agendamento(forms.ModelForm):
    class Meta:
        model = Servico_Agendamento
        exclude = ['id_agendamento']

class FormAgendamento(forms.ModelForm):
    class Meta:
        model = Agendamento
        exclude = ['id', 'cliente']
        widgets = {
            'horario': forms.TimeInput(attrs={'type':'time'}),
            'data': forms.DateInput(attrs={'type': 'date'})
        }

