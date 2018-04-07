# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-07 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flisol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='institution',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Institución'),
        ),
        migrations.AlterField(
            model_name='person',
            name='occupation',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ocupación / Profesión'),
        ),
    ]
