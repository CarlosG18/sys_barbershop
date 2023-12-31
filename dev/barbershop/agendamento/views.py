from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cadastro.models import Cliente, Gerente, Barbeiro
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
from cadastro.forms import FormBarbeiro, FormUser
from .models import Agendamento, Servico_Agendamento, Servico
from .forms import FormService, FormAgendamento, FormServico_agendamento
import logging
from django.views.generic import ListView

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
    servicos = Servico.objects.all()
    return render(request, 'agendamento/index.html', {
        "barbeiros": barbeiros,
        "servicos": servicos,
    })    

def check_agendamento(horario, data, barbeiro):
    agendamento = Agendamento.objects.filter(horario=horario,data=data, barbeiro=barbeiro).exists()
    return agendamento

def horariosOcupados(agendamentos):
    dados = []
    dias = ['segunda','terça','quarta','quinta','sexta','sabádo','domingo']
    for agendamento in agendamentos:
        info = {
            "dia": agendamento.data.day,
            "mes": agendamento.data.month,
            "ano": agendamento.data.year,
            "dia_semana": dias[agendamento.data.weekday()],
            "hora": agendamento.horario.hour,
            "minuto": agendamento.horario.minute,
            "barbeiro": agendamento.barbeiro,
        }
        dados.append(info)
    return dados


def gethoras(hr_min, hr_max):
    manha = []
    tarde = []
    noite = []
    for i in range(hr_min, hr_max):
        if i <= 12:
            hora = {
                "hora": i,
                "min": 0,
            }
            hora1 = {
                "hora": i,
                "min": 30,
            }
            manha.append(hora)
            manha.append(hora1)
        elif i <= 18:
            hora = {
                "hora": i,
                "min": 0,
            }
            hora1 = {
                "hora": i,
                "min": 30,
            }
            tarde.append(hora)
            tarde.append(hora1)
        else:
            hora = {
                "hora": i,
                "min": 0,
            }
            hora1 = {
                "hora": i,
                "min": 30,
            }
            noite.append(hora)
            noite.append(hora1)    
    return (manha,tarde,noite)

def horarios(request):
    if request.method == 'POST':
        form_agendamento = FormAgendamento(request.POST)
        form_servico = FormServico_agendamento(request.POST)
        if form_agendamento.is_valid() and form_servico.is_valid():
            check_agenda = check_agendamento(form_agendamento.cleaned_data['horario'], form_agendamento.cleaned_data['data'], form_agendamento.cleaned_data['barbeiro'])
            if not(check_agenda):
                agendamento = form_agendamento.save(commit=False)
                user = User.objects.get(username=request.user.username)
                cliente = Cliente.objects.get(user=user)
                agendamento.cliente = cliente
                agendamento.save()
                agendamento_current = Agendamento.objects.last()
                servico = form_servico.save(commit=False)
                servico.id_agendamento = agendamento_current
                servico.save()
                return HttpResponseRedirect(reverse('agendamento:index'))
            else:
                request.session['erro_agendamento'] = {
                    "name": "erro no agendamento",
                    "message": "não foi possivel concluir seu agendamento pois houve um conflito de datas e barbeiros!"
                }
                return HttpResponseRedirect(reverse('agendamento:horarios'))
    else:
        form_agendamento = FormAgendamento()
        form_servico_agendamento = FormServico_agendamento()

        services = Servico.objects.all()
        agendamentos = Agendamento.objects.all()
        barbeiros = Barbeiro.objects.all()
        
        if request.session.get('erro_agendamento'):
            dados_erro = request.session.get('erro_agendamento')
            request.session['erro_agendamento'] = None
        else:
            dados_erro = None

        manha, tarde, noite = gethoras(7,23)
        dias = ['segunda','terça','quarta','quinta','sexta','sabádo','domingo']
        horarios_ocup = horariosOcupados(agendamentos)

        return render(request, 'agendamento/data.html',{
            "agendamentos": agendamentos,
            "barbeiros": barbeiros,
            "servicos": services,
            "form_servico_agendamento": form_servico_agendamento,
            "form_agendamento": form_agendamento,
            "erro_agenda": dados_erro,
            "manha": manha,
            "tarde": tarde,
            "noite": noite,
            "dias": dias,
            "horas_ocup": horarios_ocup,
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
    user = User.objects.get(username=request.user.username)
    agendamentos = Agendamento.objects.filter(cliente__user=user)
    
    return render(request, 'agendamento/agendamentos.html', {
        "agendamentos": agendamentos,
    })

def perfil(request):
    return render(request, 'agendamento/perfil.html')

def relatorios(request):
    return render(request, 'agendamento/gerente/relatorios.html')

def Detailbarber(request, id):
    barbeiro = Barbeiro.objects.get(id=id)
    return render(request, 'agendamento/gerente/detail_barber.html', {
        "barbeiro": barbeiro,
    })

def DelBarber(request, id):
    barbeiro = Barbeiro.objects.get(id=id)
    user = User.objects.get(username=barbeiro.user.username)
    user.delete()
    barbeiro.delete()
    return HttpResponseRedirect(reverse('agendamento:barbeiros'))