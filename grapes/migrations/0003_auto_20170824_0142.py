# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 01:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grapes', '0002_auto_20170823_2342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grape',
            options={'ordering': ['name']},
        ),
    ]
