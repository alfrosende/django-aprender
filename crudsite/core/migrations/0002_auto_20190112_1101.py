# Generated by Django 2.1.4 on 2019-01-12 14:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='notas',
            field=ckeditor.fields.RichTextField(verbose_name='Notas'),
        ),
    ]
