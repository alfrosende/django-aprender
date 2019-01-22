# Generated by Django 2.1.4 on 2019-01-21 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abreviada', models.CharField(max_length=3, verbose_name='Abreviada')),
                ('descripcion', models.CharField(max_length=40, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'estado',
                'verbose_name_plural': 'estados',
                'ordering': ['abreviada'],
            },
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40, verbose_name='Titulo')),
                ('concepto', models.TextField(verbose_name='Concepto')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Estado')),
            ],
            options={
                'verbose_name': 'expediente',
                'verbose_name_plural': 'expedientes',
                'ordering': ['estado'],
            },
        ),
    ]
