# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rso', '0008_auto_20170709_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='member',
            field=models.ManyToManyField(blank=True, to='rso.RsoGroup'),
        ),
    ]
