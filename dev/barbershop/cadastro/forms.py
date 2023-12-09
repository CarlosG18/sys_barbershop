from django import forms
from .models import Cliente, Barbeiro, Gerente
from django.contrib.auth.models import User

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['user', 'type_cliente']

class FormGerente(forms.ModelForm):
    class Meta:
        model = Gerente
        exclude = ['user', 'type_cliente']

class FormBarbeiro(forms.ModelForm):
    class Meta:
        model = Barbeiro
        exclude = ['user', 'type_cliente', 'cpf_gerente']