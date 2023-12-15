from django.contrib import admin
from .models import Cliente, Barbeiro, Gerente

admin.site.register(Cliente)
admin.site.register(Barbeiro)
admin.site.register(Gerente)
