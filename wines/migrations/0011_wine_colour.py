# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0010_wine_grows_best'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='colour',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
