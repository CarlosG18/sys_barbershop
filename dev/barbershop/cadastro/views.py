from django.shortcuts import render

def index(request):
    return render(request, 'cadastro/login.html')

def cadastro(request):
    return render(request, 'cadastro/cadastro.html')

def gerente(request):
    return render(request, 'cadastro/gerente.html')
