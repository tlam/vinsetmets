# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from aliases.models import Alias
from wines.models import Style, Wine


class AliasInline(admin.TabularInline):
    model = Alias
    extra = 0


class StyleAdmin(admin.ModelAdmin):
    model = Style


class WineAdmin(admin.ModelAdmin):
    model = Wine
    filter_horizontal = ('grapes',)
    inlines = [
        AliasInline
    ]

admin.site.register(Style, StyleAdmin)
admin.site.register(Wine, WineAdmin)
