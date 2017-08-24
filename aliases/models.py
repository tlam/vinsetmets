# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Alias(models.Model):
    name = models.CharField(max_length=255, unique=True)
    wine = models.ForeignKey('wines.Wine', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
