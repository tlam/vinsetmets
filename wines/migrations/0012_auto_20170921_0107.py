# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0011_wine_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='colour',
            field=models.CharField(blank=True, choices=[('', '---'), ('red', 'Red'), ('rose', 'Rose'), ('white', 'White')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='wine',
            name='grows_best',
            field=models.ManyToManyField(blank=True, to='locations.Location'),
        ),
    ]
