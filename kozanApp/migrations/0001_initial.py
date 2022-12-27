# Generated by Django 4.1 on 2022-11-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('procesador', models.CharField(max_length=50)),
                ('grafica', models.CharField(max_length=50)),
                ('memoria', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
    ]
