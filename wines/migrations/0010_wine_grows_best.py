# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('wines', '0009_wine_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='grows_best',
            field=models.ManyToManyField(to='locations.Location'),
        ),
    ]
