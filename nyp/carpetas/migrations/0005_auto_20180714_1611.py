# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-14 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpetas', '0004_delete_tareas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carpetas',
            new_name='Gestion',
        ),
    ]
