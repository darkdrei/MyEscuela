# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sede', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institucion',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='institucion',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
