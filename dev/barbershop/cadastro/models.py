from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf_setting = RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    message="o cpf informado deverá esta no formato 999.999.999-99",
    )
    cpf = models.CharField(max_length=14, validators=[cpf_setting], unique=True)
  
    TYPE = (
      ('cli', 'cliente'),
      ('ger', 'gerente'),
      ('bar', 'barbeiro'),
    )
    type_cliente = models.CharField(max_length=3, choices=TYPE, default='cli')
    class Meta:
        abstract = True

class Cliente(Usuario):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="cliente/", default="avatar_default.png")
    
    def __str__(self):
        return f'cliente = {self.user.username}'


class Gerente(Usuario):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="gerente/", default="avatar_default.png")
    
    def __str__(self):
        return f'gerente {self.user.username}'

class Barbeiro(Usuario):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="barbeiro/", default="avatar_default.png")
    cpf_gerente = models.ForeignKey(Gerente, on_delete=models.CASCADE)

    def __str__(self):
        return f'barbeiro {self.user.username}'