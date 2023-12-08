from django.urls import path
from . import views

app_name = "agendamento"

urlpatterns = [
    path('', views.index, name='index'),
    path('horarios/', views.horarios, name='horarios'),
    path('gerente/', views.home_gerente, name='home_gerente'),
    path('gerente/cadastro/barber', views.cadastro_barber, name='cadastro_barber'),
    path('gerente/new_service/', views.new_service, name='new_service'),
    path('gerente/barbeiros/', views.barbeiros, name='barbeiros'),
    path('gerente/services', views.services, name='services'),
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('perfil/', views.perfil, name='perfil'),
]
