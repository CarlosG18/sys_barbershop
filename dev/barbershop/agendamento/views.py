from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cadastro.models import Cliente, Gerente, Barbeiro
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
from cadastro.forms import FormBarbeiro, FormUser

def get_usuario(username):
  user = User.objects.get(username=username)
  try:
    cliente = Cliente.objects.get(user=user)
    return cliente
  except ObjectDoesNotExist:
    gerente = Gerente.objects.get(user=user)
    return gerente
  
def direcion_home(request):
    user = get_usuario(request.user.username)
    if user.type_cliente == 'cli':
        return HttpResponseRedirect(reverse('agendamento:index'))
    elif user.type_cliente == 'ger':
        return HttpResponseRedirect(reverse('agendamento:home_gerente'))

@login_required
def index(request):
    barbeiros = Barbeiro.objects.all()
    return render(request, 'agendamento/index.html', {
        "barbeiros": barbeiros,
    })    

def horarios(request):
    minutos = ['00', '30']
    horarios = []
    for i in range(7, 22):
        for j in range(2):
            horarios.append(f'{i}:{minutos[j]}')

    return render(request, 'agendamento/data.html',{
        "horarios": horarios,
    })

@login_required
def home_gerente(request):
    return render(request, 'agendamento/gerente/home.html')

def cadastro_barber(request):
    gerente = Gerente.objects.get(user=request.user)
    if request.method == "POST":
        form_user = FormUser(request.POST)
        form_barbeiro = FormBarbeiro(request.POST,request.FILES)
        if form_barbeiro.is_valid() and form_user.is_valid():
            user = User.objects.create_user(username=form_user.cleaned_data["username"], email=form_user.cleaned_data["email"], password=form_user.cleaned_data["password"]) 
            user.save()
            barbeiro = form_barbeiro.save(commit=False)
            barbeiro.user = user
            barbeiro.type_cliente = 'bar'
            barbeiro.cpf_gerente = gerente
            barbeiro.save()
            return HttpResponseRedirect(reverse('agendamento:home_gerente'))
    else:
        form_user = FormUser()
        form_barbeiro = FormBarbeiro()
    return render(request, "agendamento/gerente/cadastro_barber.html",{
        "form_barbeiro": form_barbeiro,
        "form_user": form_user,
    })

def new_service(request):
    return render(request, 'agendamento/gerente/new_service.html')

def barbeiros(request):
    return render(request, 'agendamento/gerente/list_barber.html')

def services(request):
    return render(request, 'agendamento/gerente/list_services.html')

def agendamentos(request):
    return render(request, 'agendamento/agendamentos.html')

def perfil(request):
    return render(request, 'agendamento/perfil.html')

def relatorios(request):
    return render(request, 'agendamento/gerente/relatorios.html')