# Generated by Django 4.2.3 on 2023-12-08 16:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='o cpf informado deverá esta no formato 999.999.999-99', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')])),
                ('email', models.EmailField(max_length=254)),
                ('type_cliente', models.CharField(choices=[('cli', 'cliente'), ('ger', 'gerente')], default='cli', max_length=3)),
                ('img', models.ImageField(default='avatar_default.png', upload_to='gerente/')),
                ('codigo', models.TextField(max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='o cpf informado deverá esta no formato 999.999.999-99', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')])),
                ('email', models.EmailField(max_length=254)),
                ('type_cliente', models.CharField(choices=[('cli', 'cliente'), ('ger', 'gerente')], default='cli', max_length=3)),
                ('img', models.ImageField(default='avatar_default.png', upload_to='cliente/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Barbeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='o cpf informado deverá esta no formato 999.999.999-99', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$')])),
                ('email', models.EmailField(max_length=254)),
                ('type_cliente', models.CharField(choices=[('cli', 'cliente'), ('ger', 'gerente')], default='cli', max_length=3)),
                ('cpf_gerente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.gerente')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
