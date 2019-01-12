# Generated by Django 2.1.4 on 2019-01-12 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('telefono1', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono 1')),
                ('telefono2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono 2')),
                ('tipo_cliente', models.CharField(choices=[('P', 'Persona'), ('E', 'Empresa')], default='P', max_length=1, verbose_name='Tipo cliente')),
                ('cedula_identidad', models.SmallIntegerField(blank=True, null=True, verbose_name='Cedula identidad')),
                ('rut', models.SmallIntegerField(blank=True, null=True, verbose_name='RUT')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultima edicion')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('fecha', models.DateTimeField(verbose_name='Fecha de visita')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion')),
                ('notas', models.TextField(verbose_name='Notas')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultima edicion')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente', verbose_name='Cliente')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'visita',
                'verbose_name_plural': 'visitass',
                'ordering': ['-fecha'],
            },
        ),
    ]
