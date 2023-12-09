from django.urls import path
from . import views

app_name = "cadastro"

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('gerente/', views.gerente, name="gerente"),
]
