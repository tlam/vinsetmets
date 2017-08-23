# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from wines.models import Style, Wine


class StyleAdmin(admin.ModelAdmin):
    pass


class WineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Style, StyleAdmin)
admin.site.register(Wine, WineAdmin)
