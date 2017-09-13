# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Location(models.Model):
    region = models.CharField(max_length=255, blank=True, default='')
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['region', 'country']
        unique_together = (('region', 'country'),)

    def __str__(self):
        if self.region:
            return '{}, {}'.format(self.region, self.country)
        return self.country
