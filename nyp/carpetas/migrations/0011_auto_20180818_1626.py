# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpetas', '0010_auto_20180728_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productores',
            name='razon_social',
        ),
        migrations.AlterField(
            model_name='gestion',
            name='descripcion_general',
            field=models.TextField(max_length=255, null=True, blank=True),
        ),
    ]
