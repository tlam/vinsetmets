# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from grapes.models import Grape


class GrapeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Grape, GrapeAdmin)
