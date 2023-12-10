from django import forms
from .models import Servico

class FormService(forms.ModelForm):
    class Meta:
        model = Servico
        exclude = ['id']
