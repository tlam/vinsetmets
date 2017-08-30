# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from locations.models import Location


class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
