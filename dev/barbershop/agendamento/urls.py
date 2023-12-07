from django.urls import path
from . import views

app_name = "agendamento"

urlpatterns = [
    path('', views.index, name='agendamento'),
]
