# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Style(models.Model):
    name = models.CharField(max_length=255, unique=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
   

class Wine(models.Model):
    COLOUR_CHOICES = (
        ('', '---'),
        ('red', 'Red'),
        ('rose', 'Rose'),
        ('white', 'White'),
    )
    FRUIT_CHOICES = (
        (0, '---'),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    SWEETNESS_CHOICES = (
        (0, '---'),
        (1, 'Bone-Dry'),
        (2, 'Dry'),
        (3, 'Off-Dry'),
        (4, 'Sweet'),
        (5, 'Very Sweet'),
    )
    TANNIN_CHOICES = (
        (0, '---'),
        (1, 'Low'),
        (2, 'Medium-Low'),
        (3, 'Average'),
        (4, 'Astringent'),
        (5, 'Very Astringent'),
    )
    BODY_CHOICES = (
        (0, '---'),
        (1, 'Very Light'),
        (2, 'Light-Bodied'),
        (3, 'Average'),
        (4, 'Medium-Full'),
        (5, 'Full-Bodied'),
    )
    ACIDITY_CHOICES = (
        (0, '---'),
        (1, 'Low'),
        (2, 'Medium-Low'),
        (3, 'Average'),
        (4, 'Sour'),
        (5, 'Very Sour'),
    )
    ALCOHOL_CHOICES = (
        (0, '---'),
        (1, 'Low'),
        (2, 'Medium-Low'),
        (3, 'Average'),
        (4, 'Medium-High'),
        (5, 'High'),
    )

    name = models.CharField(max_length=255, unique=True)
    style = models.ForeignKey('wines.Style', on_delete=models.CASCADE)
    colour = models.CharField(max_length=100, blank=True, default='', choices=COLOUR_CHOICES)
    label = models.CharField(max_length=255, blank=True, default='')
    origin = models.CharField(max_length=255, blank=True, default='')
    grapes = models.ManyToManyField('grapes.Grape')
    fruit = models.PositiveIntegerField(default=0, choices=FRUIT_CHOICES)
    sweetness = models.PositiveIntegerField(default=0, choices=SWEETNESS_CHOICES)
    tannin = models.PositiveIntegerField(default=0, choices=TANNIN_CHOICES)
    body = models.PositiveIntegerField(default=0, choices=BODY_CHOICES)
    acidity = models.PositiveIntegerField(default=0, choices=ACIDITY_CHOICES)
    alcohol = models.PositiveIntegerField(default=0, choices=ALCOHOL_CHOICES)
    grows_best = models.ManyToManyField('locations.Location', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['style', 'name']

    def __str__(self):
        return self.name
