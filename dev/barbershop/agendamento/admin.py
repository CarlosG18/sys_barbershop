from django.contrib import admin
from .models import Servico, Agendamento

# Register your models here.
admin.site.register(Servico)
admin.site.register(Agendamento)