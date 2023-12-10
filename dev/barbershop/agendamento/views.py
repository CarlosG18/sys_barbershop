from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cadastro.models import Cliente, Gerente, Barbeiro
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
from cadastro.forms import FormBarbeiro, FormUser
from .models import Agendamento, Cliente_Agendamento, Servico_Agendamento, Servico
from .forms import FormService

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
    barbeiros = Barbeiro.objects.all()
    services = Servico.objects.all()

    dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabádo', 'domingo']
    minutos = ['00', '30']
    horarios = []
    data_agendamento = []

    for i in range(7, 22):
        for j in range(2):
            horarios.append(f'{i}:{minutos[j]}')

    agendamentos = Agendamento.objects.all()

    for hora in horarios:
        d = []
        data = {
            "hora": hora,
        }
        for dia in dias:
            status = {
                "dia": dia,
                "status": False,
            }
            d.append(status)
        data['disponibilidade'] = d
        data_agendamento.append(data)

    return render(request, 'agendamento/data.html',{
        "agendamentos": agendamentos,
        "horarios": horarios,
        "data_agendamento": data_agendamento,
        "dias": dias,
        "barbeiros": barbeiros,
        "servicos": services,
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
    if request.method == "POST":
        form_service = FormService(request.POST)
        if form_service.is_valid():
            form_service.save()
            return HttpResponseRedirect(reverse('agendamento:home_gerente'))
    else:
        form_service = FormService()
    return render(request, 'agendamento/gerente/new_service.html', {
        "form_service": form_service,
    })

def barbeiros(request):
    barbeiros = Barbeiro.objects.all()
    return render(request, 'agendamento/gerente/list_barber.html', {
        "barbeiros": barbeiros
    })

def services(request):
    services = Servico.objects.all()
    return render(request, 'agendamento/gerente/list_services.html', {
        "servicos" : services,
    })

def agendamentos(request):

    return render(request, 'agendamento/agendamentos.html')

def perfil(request):
    return render(request, 'agendamento/perfil.html')

def relatorios(request):
    return render(request, 'agendamento/gerente/relatorios.html')