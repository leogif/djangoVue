# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-14 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_auto_20190512_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='empregado',
            name='foto',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]