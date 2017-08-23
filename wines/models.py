# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Style(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
   

class Wine(models.Model):
    name = models.CharField(max_length=255, unique=True)
    style = models.ForeignKey('wines.Style', on_delete=models.CASCADE)
    label = models.CharField(max_length=10, default='')
    vintage = models.PositiveIntegerField(default=0)
    origin = models.CharField(max_length=255, blank=True, default='')
    grapes = models.ManyToManyField('grapes.Grape')
    fruit = models.PositiveIntegerField(default=0)
    sweetness = models.PositiveIntegerField(default=0)
    tannin = models.PositiveIntegerField(default=0)
    body = models.PositiveIntegerField(default=0)
    acidity = models.PositiveIntegerField(default=0)
    alcohol = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['style', 'name']

    def __str__(self):
        return self.name
