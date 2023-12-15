from django.contrib import admin
from .models import Servico, Agendamento, Servico_Agendamento

# Register your models here.
admin.site.register(Servico)
admin.site.register(Agendamento)
admin.site.register(Servico_Agendamento)