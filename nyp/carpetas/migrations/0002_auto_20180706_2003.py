# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-06 23:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carpetas', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Facturas',
        ),
        migrations.DeleteModel(
            name='Liquidacion',
        ),
        migrations.DeleteModel(
            name='Pagos',
        ),
        migrations.DeleteModel(
            name='Presupuesto',
        ),
        migrations.AlterModelOptions(
            name='clientes',
            options={},
        ),
        migrations.RenameField(
            model_name='carpetas',
            old_name='descripcion',
            new_name='descripcion_general',
        ),
        migrations.RenameField(
            model_name='carpetas',
            old_name='tipo',
            new_name='nombre',
        ),
        migrations.AddField(
            model_name='carpetas',
            name='compania_asegurado',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carpetas',
            name='compania_tercero',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carpetas',
            name='liquidacion_del_cliente',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='carpetas',
            name='media',
            field=models.FileField(blank=True, help_text='Adjuntar archivo', null=True, upload_to='Mi Carpeta/'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='razon_social',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='responsable',
            field=models.CharField(blank=True, help_text='Ingrese el nombre del contacto responsable de llevar el caso por parte de la empresa', max_length=255, null=True),
        ),
    ]
