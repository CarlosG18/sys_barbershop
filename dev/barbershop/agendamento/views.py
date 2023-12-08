from django.shortcuts import render

def index(request):
    return render(request, 'agendamento/index.html')

def horarios(request):
    minutos = ['00', '30']
    horarios = []
    for i in range(7, 22):
        for j in range(2):
            horarios.append(f'{i}:{minutos[j]}')

    return render(request, 'agendamento/data.html',{
        "horarios": horarios,
    })

def home_gerente(request):
    return render(request, 'agendamento/gerente/home.html')

def cadastro_barber(request):
    return render(request, 'agendamento/gerente/cadastro_barber.html')

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