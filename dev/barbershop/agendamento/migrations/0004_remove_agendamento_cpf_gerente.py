# Generated by Django 4.2.3 on 2023-12-12 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0003_agendamento_data_alter_agendamento_horario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='cpf_gerente',
        ),
    ]
