# Generated by Django 4.2.3 on 2023-12-27 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_remove_gerente_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barbeiro',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gerente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
