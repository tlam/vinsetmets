# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Cuisine(models.Model):
    name = models.CharField(max_length=255, unique=True)
    origin = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default='', blank=True)
    image = models.URLField(default='', blank=True)
    cuisine = models.ForeignKey('cuisines.Cuisine', related_name='foods')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
