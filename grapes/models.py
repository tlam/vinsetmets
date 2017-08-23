# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Grape(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
