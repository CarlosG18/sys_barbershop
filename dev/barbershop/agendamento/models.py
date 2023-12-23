from django.db import models
from cadastro.models import Gerente, Cliente, Barbeiro

class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    horario = models.TimeField()
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)

    def __str__(self):
        return f'agendamento no horario {self.horario}'

class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'serviço {self.nome} - preço R${self.preco}'

class Servico_Agendamento(models.Model):
    id_agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    id_servico = models.ForeignKey(Servico, on_delete=models.CASCADE)