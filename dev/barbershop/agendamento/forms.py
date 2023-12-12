from django import forms
from .models import Servico, Servico_Agendamento, Agendamento, Cliente_Agendamento

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
        exclude = ['id', 'cpf_gerente']
        widgets = {
            'horario': forms.TimeInput(attrs={'type':'time'}),
            'data': forms.DateInput(attrs={'type': 'date'})
        }

class FormCliente_agendamento(forms.ModelForm):
    class Meta:
        model = Cliente_Agendamento
        exclude = ['cpf_cliente', 'id_agendamento']

