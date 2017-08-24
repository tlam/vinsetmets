# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0006_auto_20170824_0142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='style',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='style',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wine',
            name='acidity',
            field=models.PositiveIntegerField(choices=[(0, '---'), (1, 'Low'), (2, 'Medium-Low'), (3, 'Average'), (4, 'Sour'), (5, 'Very Sour')], default=0),
        ),
        migrations.AlterField(
            model_name='wine',
            name='alcohol',
            field=models.PositiveIntegerField(choices=[(0, '---'), (1, 'Low'), (2, 'Medium-Low'), (3, 'Average'), (4, 'Medium-High'), (5, 'High')], default=0),
        ),
        migrations.AlterField(
            model_name='wine',
            name='body',
            field=models.PositiveIntegerField(choices=[(0, '---'), (1, 'Very Light'), (2, 'Light-Bodied'), (3, 'Average'), (4, 'Medium-Full'), (5, 'Full-Bodied')], default=0),
        ),
        migrations.AlterField(
            model_name='wine',
            name='fruit',
            field=models.PositiveIntegerField(choices=[(0, '---'), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='wine',
            name='sweetness',
            field=models.PositiveIntegerField(choices=[(0, '---'), (1, 'Bone-Dry'), (2, 'Dry'), (3, 'Off-Dry'), (4, 'Sweet'), (5, 'Very Sweet')], default=0),
        ),
        migrations.AlterField(
            model_name='wine',
            name='tannin',
            field=models.PositiveIntegerField(choices=[(0, '---'), (1, 'Low'), (2, 'Medium-Low'), (3, 'Average'), (4, 'Astringent'), (5, 'Very Astringent')], default=0),
        ),
    ]