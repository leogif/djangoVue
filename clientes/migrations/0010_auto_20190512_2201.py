# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-13 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20190512_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empregado',
            name='idade',
            field=models.IntegerField(),
        ),
    ]
